$(function() {
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    headerToolbar: {
      left: 'today',
      center: 'title',
      right: 'prev,next'
    },
    dateClick: function(info) {
      //$("#schedule_date").html(info.dateStr)
      $.ajax(
        {
          type: "GET",
          url: "/scheduling/patrol_schedule",
          success: function(result){
            $("#schedule_date").html('{{test_date}}')
          }
        }
      )
      // change the day's background color 
      //info.dayEl.style.backgroundColor = 'red';
    }
  });
  calendar.render();
  $('#my-button').on('click',function() {
    var date = calendar.getDate();
    alert("The current date of the calendar is " + date.toString());
    
  });

  
});
