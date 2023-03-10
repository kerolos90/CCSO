// $(function() {
//   var calendarEl = document.getElementById('calendar');
//   var calendar = new FullCalendar.Calendar(calendarEl, {
//     initialView: 'dayGridMonth',
//     headerToolbar: {
//       left: 'today',
//       center: 'title',
//       right: 'prev,next'
//     },
//     events : [],

//     dateClick: function (date) {
//       $("#table-to-refresh").load("/scheduling/patrol_schedule")
//       $("#schedule_date").html(date.dateStr)
//       $("#table-to-refresh").load("/scheduling/patrol_schedule",
//         { date: date.dateStr, csrfmiddlewaretoken: '{{ csrf_token }}' })
//       console.log(date.dateStr)
//     }
//   });
//   calendar.render();
  
// });
