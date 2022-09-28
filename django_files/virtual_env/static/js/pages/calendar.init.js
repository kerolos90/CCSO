!(function (s) {
  "use strict";
  function e() { }
  (e.prototype.init = function () {
    var n = s("#event-modal"),
      t = s("#modal-title"),
      a = s("#form-event"),
      l = null,
      i = null,
      o = document.getElementsByClassName("needs-validation"),
      l = null,
      i = null,
      e = new Date();
    e.getDate(), e.getMonth(), e.getFullYear();
    new FullCalendarInteraction.Draggable(
      document.getElementById("external-events"),
      {
        itemSelector: ".external-event",
        eventData: function (e) {
          return { title: e.innerText, className: s(e).data("class") };
        },
      }
    );
    document.getElementById("external-events");
    e = document.getElementById("calendar");
    function r(e) {
      n.modal("show"),
        a.removeClass("was-validated"),
        a[0].reset(),
        s("#event-title").val(),
        s("#event-category").val(),
        t.text("Add Event"),
        (i = e);
    }
    var d = new FullCalendar.Calendar(e, {
      plugins: ["bootstrap", "interaction", "dayGrid", "timeGrid"],
      editable: !0,
      droppable: !0,
      selectable: !0,
      defaultView: "dayGridMonth",
      themeSystem: "bootstrap",
      header: { left: "today ", center: "title", right: "prev,next" },
      eventClick: function (e) {
        n.modal("show"),
          a[0].reset(),
          (l = e.event),
          s("#event-title").val(l.title),
          s("#event-category").val(l.classNames[0]),
          (i = null),
          t.text("Edit Event"),
          (i = null);
      },
      dateClick: function (e) {
        r(e);
      },
      events: [],
    });
    d.render(),
      s(a).on("submit", function (e) {
        e.preventDefault();
        s("#form-event :input");
        var t = s("#event-title").val(),
          e = s("#event-category").val();
        !1 === o[0].checkValidity()
          ? (event.preventDefault(),
            event.stopPropagation(),
            o[0].classList.add("was-validated"))
          : (l
            ? (l.setProp("title", t), l.setProp("classNames", [e]))
            : ((e = {
              title: t,
              start: i.date,
              allDay: i.allDay,
              className: e,
            }),
              d.addEvent(e)),
            n.modal("hide"));
      }),
      s("#btn-delete-event").on("click", function (e) {
        l && (l.remove(), (l = null), n.modal("hide"));
      }),
      s("#btn-new-event").on("click", function (e) {
        r({ date: new Date(), allDay: !0 });
      });
  }),
    (s.CalendarPage = new e()),
    (s.CalendarPage.Constructor = e);

})(window.jQuery),
  (function () {
    "use strict";
    window.jQuery.CalendarPage.init();
  })();
