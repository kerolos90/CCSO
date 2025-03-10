!(function (a) {
  "use strict";
  var e,
    t,
    n,
    o = localStorage.getItem("minia-language"),
    r = "en";
  function d() {
    var t = document.querySelectorAll(".counter-value");
    t.forEach(function (o) {
      !(function t() {
        var e = +o.getAttribute("data-target"),
          a = +o.innerText,
          n = e / 250;
        n < 1 && (n = 1),
          a < e
            ? ((o.innerText = (a + n).toFixed(0)), setTimeout(t, 1))
            : (o.innerText = e);
      })();
    });
  }
  function l() {
    for (
      var t = document
          .getElementById("topnav-menu-content")
          .getElementsByTagName("a"),
        e = 0,
        a = t.length;
      e < a;
      e++
    )
      t[e] &&
        t[e].parentElement &&
        "nav-item dropdown active" ===
          t[e].parentElement.getAttribute("class") &&
        (t[e].parentElement.classList.remove("active"),
        t[e].nextElementSibling &&
          t[e].nextElementSibling.classList.remove("show"));
  }
  function s(t) {
  }
  function c() {
    document.webkitIsFullScreen ||
      document.mozFullScreen ||
      document.msFullscreenElement ||
      a("body").removeClass("fullscreen-enable");
  }
  a("#side-menu").metisMenu(),
    d(),
    (e = document.body.getAttribute("data-sidebar-size")),
    a(window).on("load", function () {
      a(".switch").on("switch-change", function () {
        toggleWeather();
      }),
        1024 <= window.innerWidth &&
          window.innerWidth <= 1366 &&
          (document.body.setAttribute("data-sidebar-size", "sm"),
          s("sidebar-size-small"));
    }),
    a("#vertical-menu-btn").on("click", function (t) {
      t.preventDefault(),
        a("body").toggleClass("sidebar-enable"),
        992 <= a(window).width() &&
          (null == e
            ? null == document.body.getAttribute("data-sidebar-size") ||
              "lg" == document.body.getAttribute("data-sidebar-size")
              ? document.body.setAttribute("data-sidebar-size", "sm")
              : document.body.setAttribute("data-sidebar-size", "lg")
            : "md" == e
            ? "md" == document.body.getAttribute("data-sidebar-size")
              ? document.body.setAttribute("data-sidebar-size", "sm")
              : document.body.setAttribute("data-sidebar-size", "md")
            : "sm" == document.body.getAttribute("data-sidebar-size")
            ? document.body.setAttribute("data-sidebar-size", "lg")
            : document.body.setAttribute("data-sidebar-size", "sm"));
    }),
    a("#sidebar-menu a").each(function () {
      var t = window.location.href.split(/[?#]/)[0];
      this.href == t &&
        (a(this).addClass("active"),
        a(this).parent().addClass("mm-active"),
        a(this).parent().parent().addClass("mm-show"),
        a(this).parent().parent().prev().addClass("mm-active"),
        a(this).parent().parent().parent().addClass("mm-active"),
        a(this).parent().parent().parent().parent().addClass("mm-show"),
        a(this)
          .parent()
          .parent()
          .parent()
          .parent()
          .parent()
          .addClass("mm-active"));
    }),
    a(document).ready(function () {
      var t;
      0 < a("#sidebar-menu").length &&
        0 < a("#sidebar-menu .mm-active .active").length &&
        300 < (t = a("#sidebar-menu .mm-active .active").offset().top) &&
        ((t -= 300),
        a(".vertical-menu .simplebar-content-wrapper").animate(
          { scrollTop: t },
          "slow"
        ));
    }),
    [].slice
      .call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
      .map(function (t) {
        return new bootstrap.Tooltip(t);
      }),
    [].slice
      .call(document.querySelectorAll('[data-bs-toggle="popover"]'))
      .map(function (t) {
        return new bootstrap.Popover(t);
      }),
    [].slice.call(document.querySelectorAll(".toast")).map(function (t) {
      return new bootstrap.Toast(t);
    }),
    window.sessionStorage &&
      ((t = sessionStorage.getItem("is_visited"))
        ? a("#" + t).prop("checked", !0)
        : sessionStorage.setItem("is_visited", "layout-ltr")),
    o && "null" != o && o !== r && i(o),
    a(".language").on("click", function (t) {
      i(a(this).attr("data-lang"));
    }),
    a(window).on("load", function () {
      a("#status").fadeOut(), a("#preloader").delay(350).fadeOut("slow");
    }),
    (n = document.getElementsByTagName("body")[0]),
    a(".right-bar-toggle").on("click", function (t) {
      a("body").toggleClass("right-bar-enabled");
    }),
    a(document).on("click", "body", function (t) {
      0 < a(t.target).closest(".right-bar-toggle, .right-bar").length ||
        a("body").removeClass("right-bar-enabled");
    }),
    n.hasAttribute("data-layout") &&
    "horizontal" == n.getAttribute("data-layout")
      ? (s("layout-horizontal"), a(".sidebar-setting").hide())
      : s("layout-vertical"),
    n.hasAttribute("data-layout-mode") &&
    "dark" == n.getAttribute("data-layout-mode")
      ? s("layout-mode-dark")
      : s("layout-mode-light"),
    n.hasAttribute("data-layout-size") &&
    "boxed" == n.getAttribute("data-layout-size")
      ? s("layout-width-boxed")
      : s("layout-width-fuild"),
    n.hasAttribute("data-layout-scrollable") &&
    "true" == n.getAttribute("data-layout-scrollable")
      ? s("layout-position-scrollable")
      : s("layout-position-fixed"),
    n.hasAttribute("data-topbar") && "dark" == n.getAttribute("data-topbar")
      ? s("topbar-color-dark")
      : s("topbar-color-light"),
    n.hasAttribute("data-sidebar-size") &&
    "sm" == n.getAttribute("data-sidebar-size")
      ? s("sidebar-size-small")
      : n.hasAttribute("data-sidebar-size") &&
        "md" == n.getAttribute("data-sidebar-size")
      ? s("sidebar-size-compact")
      : s("sidebar-size-default"),
    n.hasAttribute("data-sidebar") && "brand" == n.getAttribute("data-sidebar")
      ? s("sidebar-color-brand")
      : n.hasAttribute("data-sidebar") &&
        "dark" == n.getAttribute("data-sidebar")
      ? s("sidebar-color-dark")
      : s("sidebar-color-light"),
    document.getElementsByTagName("html")[0].hasAttribute("dir") &&
    "rtl" == document.getElementsByTagName("html")[0].getAttribute("dir")
      ? s("layout-direction-rtl")
      : s("layout-direction-ltr"),
    a("input[name='layout']").on("change", function () {
      window.location.href =
        "vertical" == a(this).val() ? "index.html" : "layouts-horizontal.html";
    }),
    a("input[name='layout-mode']").on("change", function () {
      "light" == a(this).val()
        ? (document.body.setAttribute("data-layout-mode", "light"),
          document.body.setAttribute("data-topbar", "light"),
          document.body.setAttribute("data-sidebar", "light"),
          (n.hasAttribute("data-layout") &&
            "horizontal" == n.getAttribute("data-layout")) ||
            document.body.setAttribute("data-sidebar", "light"),
          s("topbar-color-light"),
          s("sidebar-color-light"))
        : (document.body.setAttribute("data-layout-mode", "dark"),
          document.body.setAttribute("data-topbar", "dark"),
          document.body.setAttribute("data-sidebar", "dark"),
          (n.hasAttribute("data-layout") &&
            "horizontal" == n.getAttribute("data-layout")) ||
            document.body.setAttribute("data-sidebar", "dark"),
          s("topbar-color-dark"),
          s("sidebar-color-dark"));
    }),
    a("input[name='layout-direction']").on("change", function () {
      "ltr" == a(this).val()
        ? (document.getElementsByTagName("html")[0].removeAttribute("dir"),
          document
            .getElementById("bootstrap-style")
            .setAttribute("href", "assets/css/bootstrap.min.css"),
          document
            .getElementById("app-style")
            .setAttribute("href", "assets/css/app.min.css"))
        : (document
            .getElementById("bootstrap-style")
            .setAttribute("href", "assets/css/bootstrap-rtl.min.css"),
          document
            .getElementById("app-style")
            .setAttribute("href", "assets/css/app-rtl.min.css"),
          document.getElementsByTagName("html")[0].setAttribute("dir", "rtl"));
    }),
    a(".table-check .form-check-input").change(function () {
      a(".table-check .form-check-input:checked").length ==
      a(".table-check .form-check-input").length
        ? a("#checkAll").prop("checked", !0)
        : a("#checkAll").prop("checked", !1);
    });
})(jQuery),
  feather.replace();
