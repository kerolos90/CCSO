document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    headerToolbar: {
      left: 'today',
      center: 'title',
      right: 'prev,next'
    },
  });
  calendar.render();
  document.getElementById('my-button').addEventListener('click', function() {
    var date = calendar.getDate();
    alert("The current date of the calendar is " + date.toString());
  });
});
