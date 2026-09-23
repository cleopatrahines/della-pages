(function () {
  "use strict";

  var ROOT_SELECTOR = "[data-della-compare]";
  var TAB_SELECTOR = "[role='tab'][data-tab-target]";
  var initializedRoots = new WeakSet();

  function getTabs(tabList) {
    return Array.prototype.slice.call(tabList.querySelectorAll(TAB_SELECTOR));
  }

  function activateTab(root, tab, moveFocus) {
    var tabList = tab.closest("[data-system-tabs]");
    var tabs = getTabs(tabList);
    var targetId = tab.getAttribute("data-tab-target");

    tabs.forEach(function (candidate) {
      var isActive = candidate === tab;
      var panelId = candidate.getAttribute("data-tab-target");
      var panel = root.querySelector("#" + panelId);

      candidate.setAttribute("aria-selected", isActive ? "true" : "false");
      candidate.setAttribute("tabindex", isActive ? "0" : "-1");
      if (panel) panel.hidden = !isActive;
    });

    Array.prototype.forEach.call(
      root.querySelectorAll("[data-collection-target]"),
      function (link) {
        link.hidden = link.getAttribute("data-collection-target") !== targetId;
      }
    );

    root.setAttribute("data-active-system", targetId);
    if (moveFocus) tab.focus();
  }

  function onTabKeydown(event, root, tabs) {
    var currentIndex = tabs.indexOf(event.currentTarget);
    var nextIndex = currentIndex;

    if (event.key === "ArrowRight") nextIndex = (currentIndex + 1) % tabs.length;
    else if (event.key === "ArrowLeft") nextIndex = (currentIndex - 1 + tabs.length) % tabs.length;
    else if (event.key === "Home") nextIndex = 0;
    else if (event.key === "End") nextIndex = tabs.length - 1;
    else return;

    event.preventDefault();
    activateTab(root, tabs[nextIndex], true);
  }

  function initializeTabList(root, tabList) {
    var tabs = getTabs(tabList);
    if (!tabs.length) return;

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () { activateTab(root, tab, false); });
      tab.addEventListener("keydown", function (event) { onTabKeydown(event, root, tabs); });
    });

    activateTab(root, tabs.find(function (tab) {
      return tab.getAttribute("aria-selected") === "true";
    }) || tabs[0], false);
  }

  function initializeDiagramZoom(root) {
    var dialog = document.querySelector("[data-diagram-dialog]");
    var triggers = root.querySelectorAll("[data-diagram-zoom]");
    if (!dialog || !triggers.length || typeof dialog.showModal !== "function") return;

    var dialogImage = dialog.querySelector("[data-diagram-image]");
    var dialogCaption = dialog.querySelector("[data-diagram-caption]");
    var closeButton = dialog.querySelector("[data-diagram-close]");

    function closeDialog() {
      if (dialog.open) dialog.close();
    }

    Array.prototype.forEach.call(triggers, function (trigger) {
      trigger.addEventListener("click", function () {
        var figure = trigger.closest("figure");
        var image = figure ? figure.querySelector("img") : null;
        if (!image) return;

        if (dialogImage) {
          dialogImage.src = image.currentSrc || image.src;
          dialogImage.alt = image.alt || "";
        }
        if (dialogCaption) {
          var note = figure.querySelector(".della-compare__diagram-note");
          dialogCaption.textContent = note ? note.textContent : "";
        }
        dialog.showModal();
      });
    });

    if (closeButton) closeButton.addEventListener("click", closeDialog);
    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) closeDialog();
    });
  }

  function initializeQuickCompare(root) {
    var section = root.querySelector("[data-quick-compare]");
    if (!section) return;
    var tabs = Array.from(section.querySelectorAll("[role='tab']"));
    function select(tab, focus) {
      tabs.forEach(function (item) {
        var active = item === tab;
        item.setAttribute("aria-selected", String(active));
        item.tabIndex = active ? 0 : -1;
        section.querySelector("#" + item.getAttribute("aria-controls")).hidden = !active;
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (tab, index) {
      tab.addEventListener("click", function () { select(tab, false); });
      tab.addEventListener("keydown", function (event) {
        var next = index;
        if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
        else if (event.key === "ArrowLeft") next = (index + tabs.length - 1) % tabs.length;
        else if (event.key === "Home") next = 0;
        else if (event.key === "End") next = tabs.length - 1;
        else return;
        event.preventDefault();
        select(tabs[next], true);
      });
    });
    select(tabs[0], false);
    section.setAttribute("data-ready", "");
  }

  function initializeProjectExplorer(root) {
    var section = root.querySelector("[data-project-explorer]");
    if (!section) return;
    var tabs = Array.from(section.querySelectorAll("[data-project-tab]"));
    var panels = Array.from(section.querySelectorAll("[data-project-panel]"));
    var thumbs = Array.from(section.querySelectorAll("[data-project-thumb]"));
    section.querySelector(".della-compare__project-tabs").setAttribute("role", "tablist");
    function select(index, focus) {
      tabs.forEach(function (tab, i) {
        var active = i === index;
        tab.setAttribute("role", "tab");
        tab.setAttribute("aria-selected", String(active));
        tab.tabIndex = active ? 0 : -1;
        panels[i].setAttribute("role", "tabpanel");
        panels[i].tabIndex = 0;
        panels[i].hidden = !active;
        thumbs[i].setAttribute("aria-pressed", String(active));
      });
      if (focus) tabs[index].focus({ preventScroll: true });
    }
    tabs.forEach(function (tab, index) {
      tab.addEventListener("click", function () { select(index, false); });
      tab.addEventListener("keydown", function (event) {
        var next = index;
        if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
        else if (event.key === "ArrowLeft") next = (index + tabs.length - 1) % tabs.length;
        else if (event.key === "Home") next = 0;
        else if (event.key === "End") next = tabs.length - 1;
        else return;
        event.preventDefault();
        select(next, true);
      });
      thumbs[index].addEventListener("click", function () { select(index, false); });
    });
    select(0, false);
    section.setAttribute("data-ready", "");
  }

  function initializeRoot(root) {
    if (initializedRoots.has(root)) return;
    initializedRoots.add(root);

    Array.prototype.forEach.call(
      root.querySelectorAll("[data-system-tabs]"),
      function (tabList) { initializeTabList(root, tabList); }
    );

    root.classList.add("della-compare--enhanced");
    initializeDiagramZoom(root);
    initializeQuickCompare(root);
    initializeProjectExplorer(root);
  }

  function initializeWithin(scope) {
    if (scope.matches && scope.matches(ROOT_SELECTOR)) initializeRoot(scope);
    Array.prototype.forEach.call(
      scope.querySelectorAll ? scope.querySelectorAll(ROOT_SELECTOR) : [],
      initializeRoot
    );
  }

  function start() { initializeWithin(document); }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start, { once: true });
  } else {
    start();
  }

  document.addEventListener("shopify:section:load", function (event) {
    initializeWithin(event.target);
  });
}());
