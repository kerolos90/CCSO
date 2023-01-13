$(function() {
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    headerToolbar: {
      left: 'today',
      center: 'title',
      right: 'prev,next'
    },
    events : [],

    dateClick: function(date) {
      $("#schedule_date").html(date.dateStr)
      $("#table-to-refresh").load("/scheduling/patrol_schedule")
    }
  });
  calendar.render();
  
});
