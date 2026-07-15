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

  function initializeRoot(root) {
    if (initializedRoots.has(root)) return;
    initializedRoots.add(root);

    Array.prototype.forEach.call(
      root.querySelectorAll("[data-system-tabs]"),
      function (tabList) { initializeTabList(root, tabList); }
    );

    root.classList.add("della-compare--enhanced");
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
