!(function ($) {
  "use strict";

  var CalendarPage = function () {};

  (CalendarPage.prototype.init = function () {
    var addEvent = $("#event-modal");
    /* initialize the calendar */
    var calendarEl = document.getElementById("calendar");

    var calendar = new FullCalendar.Calendar(calendarEl, {
      plugins: ["bootstrap", "interaction", "dayGrid", "timeGrid"],
      defaultView: "dayGridMonth",
      themeSystem: "bootstrap",
      header: {
        left: "today ",
        center: "title",
        right: "prev,next",
      },
      eventSources: [
        {
          events: [
            {
              start: '2022-10-10',
              rendering: 'background',
            },
            {
              start: '2022-10-11',
              rendering: 'background',
            },
            {
              start: '2022-10-14',
              rendering: 'background',
            },
            {
              start: '2022-10-15',
              rendering: 'background',
            },
            {
              start: '2022-10-16',
              rendering: 'background',
            }
          ],
          rendering: 'background',
          backgroundColor: '#7b3f00 '
        },
        {
          events: [
            {
              start: '2022-10-12',
              rendering: 'background',
            },
            {
              start: '2022-10-13',
              rendering: 'background',
            }
          ],
          rendering: 'background',
          backgroundColor: 'gold'
        }
      ],   
      dateClick: function (info) {
        addEvent.modal("show");

        console.log(info.dateStr);
      },
    });
    calendar.render();
  }),
    //init
     ($.CalendarPage = new CalendarPage()),
     ($.CalendarPage.Constructor = CalendarPage);
})(window.jQuery),
  //initializing
  (function ($) {
  "use strict";
     $.CalendarPage.init();
  })(window.jQuery);

