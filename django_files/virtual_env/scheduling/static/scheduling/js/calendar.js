$(function() {
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    headerToolbar: {
      left: 'today',
      center: 'title',
      right: 'prev,next'
    },
    dateClick: function(date) {
      $("#schedule_date").html(date.dateStr)
        // $.ajax(
        //   {
        //     type: "GET",
        //     url: "/scheduling/patrol_schedule",
        //     success: function(data){
        //      $('#table-to-refresh').empty() 
        //     $('#table-to-refresh').replaceWith(data)
             
        //     }
            
        //   }
        // )
      $("#table-to-refresh").load("/scheduling/patrol_schedule")
      // change the day's background color 
    day.dayEl.style.backgroundColor = 'red';
    }
  });
  calendar.render();
  
});
