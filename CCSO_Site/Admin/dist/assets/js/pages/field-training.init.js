//DOR categories
const categories = {
    "1. Appearance": "Physical appearance, dress, and demeanor.",
    "2. Attitude": "Interaction between Probationary Officer and FTO, Probationary Officer and individuals in the community.",
    "3. Motor Vehicle Operations": "Competence in operating a police vehicle during general patrol and emergency situations.",
    "4. Orientation": "Competence to respond to common geographical areas, locations and businesses.",
    "5. Field Performance: Non-Stress": "Ability to perform routine, non-stress police activities.",
    "6. Field Performance: Stress": "Ability to perform in moderate and high stress situations.",
    "7. Written Comm. (Report Writing)": "Ability to take detailed field notes and write reports with no assistance",
    "8. Investigative Skill/ Case Building": "Understand the necessity of the four building blocks and fulfill those on each case.",
    "9. Directed Patrol/SIFA": "Probationary Officer interest, and ability, to initiate proactive patrol activity; ability to recognize, analyze, and take action in law enforcement related activities.",
    "10. Officer Safety": "Ability to perform police tasks without injuring self or others, or exposing self or others to unnecessary danger/risk.",
    "11. Radio/ Telecommunications": "Ability to effectively use law enforcement communications and other equipment.",
    "12. Technology/ MDC": "Ability to perform police tasks while utilizing readily available equipment and follow established protocol.",
    "13. Knowledge/Application of Criminal Law": "Knowledge of the criminal statutes, criminal procedures, including laws of arrest and  search/seizure.",
    "14. Traffic Laws": "Knowledge of the vehicle code and evaluates the officer’s ability to apply that knowledge in field situations.",
    "15. Department Policies/ Procedures": "Knowledge of/ability to apply the Urbana Champaign County Sheriff’s Office’s policies, procedures, general or special orders and acceptable past practices.",
    "16. Relationships": "Interaction with individuals in the Community and persons within the Department environment."
};

//Report Evaluation questions
const eval_questions = ["The information in this report is factual and organized", "Unnecessary information has been eliminated",
                        "This report is concisely written", "This report is clear and understandable",
                        "This report is complete for this set of facts", "The writing in this report is legible", "This report was completed in appropriate time",
                        "This report is grammatically and structurally correct", "This report is acceptable"];

//Daily Forms                        
$("#day-modal-body").append(
       `                           <nav>
                                <div class="nav nav-tabs" id="nav-tab" role="tablist">
                                    <button class="nav-link active" id="nav-day-1-dor" data-bs-toggle="tab" data-bs-target="#day-1-dor"
                                        type="button" role="tab" aria-controls="day-1-dor" aria-selected="true">
                                        Daily Observation Report (DOR)
                                    </button>
                                    <button class="nav-link" id="nav-day-1-plog" data-bs-toggle="tab" data-bs-target="#day-1-plog" type="button"
                                        role="tab" aria-controls="day-1-plog" aria-selected="true">
                                        Patrol Activity Log
                                    </button>
                                    <button class="nav-link" id="nav-day-1-coversheet" data-bs-toggle="tab" data-bs-target="#day-1-coversheet" type="button"
                                        role="tab" aria-controls="day-1-coversheet" aria-selected="true">
                                        Report Cover Sheet
                                    </button>
                                    <button class="nav-link" id="nav-day-1-misc" data-bs-toggle="tab" data-bs-target="#day-1-misc" type="button"
                                        role="tab" aria-controls="day-1-misc" aria-selected="true">
                                        Misc.
                                    </button>
                                </div>
                            </nav>
                            <div class="tab-content" id="nav-tabContent">
                                <div class="tab-pane fade show active" id="day-1-dor" role="tabpanel" aria-labelledby="nav-day-1-dor">
                                    <br>
                                    <div class="card shadow">
                                        <div class="card-header d-flex justify-content-center">
                                            <table class="table table-borderless" style="width:50%">
                                                <tbody>
                                                    <tr class="text-center">
                                                    <th colspan="4"scope="row">Day Worked: <input class="form-control" type="date" value="2019-08-19" id="example-date-input"></th>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">Field Training Officer (FTO):</th>
                                                        <td >
                                                            <select class="form-select">
                                                                <option>Select</option>
                                                            </select>
                                                        </td>
                                                        <th scope="row">Probationary Deputy:</th>
                                                        <td >
                                                            <select class="form-select">
                                                                <option>Select</option>
                                                            </select>
                                                        </td>
                                                    </tr>
                                                    
                                                    <tr>
                                                        <th scope="row">Phase:</th>
                                                        <td>1</td>
                                                        <th scope="row">DOR #:</th>
                                                        <td><input class="form-control" type="number" value="1" id="example-number-input"></td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">Hours Worked:</th>
                                                        <td><input class="form-control" type="number" value="12" id="example-number-input"></td>
                                                        <th scope="row">Beat:</th>
                                                        <td >
                                                            <select class="form-select">
                                                                <option>1/2</option>
                                                                <option>3/4</option>
                                                                <option>4/5</option>
                                                                <option>5/6</option>
                                                                <option>7/8</option>
                                                            </select>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>

                                        <div class="card-body">
                                            <table class="table table-bordered">
                                                <thead>
                                                    <tr class="text-center">
                                                        <th colspan="6">Legend</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>1: Unacceptable</td>
                                                        <td>4: Acceptable</td>
                                                        <td>7: Superior</td>
                                                        <td>NO: Not Observed</td>
                                                        <td>NRT: Not Responding to Training</td>
                                                        <td>NAR: Narative</td>                                                       
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <br>
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th style="width: 50%;" scope="col">Category</th>
                                                        <th style="width: 10%;" scope="col">Evaluation Scale</th>
                                                        <th style="width: 10%;" scope="col">Training Time</th>
                                                    </tr>
                                                </thead>
                                                <tbody id="day-1-dor-body">                                         
                                                </tbody>
                                            </table>
                                            <h6 class="text-end pe-5">Total Training Time: 45 Minutes</h6>
                                            <br>
                                            <div>   This form is to be filled out in its entirety each day. Comment on the most and least satisfactory performance of the day. 
                                                    Narrative comments (NAR) are required on the reverse side of the form for any performance less than 3 or greater than 5. 
                                                    Document all remedial training (REM) in minutes. Any check of Not Responding to Training (NRT) requires a referral form with recommendations for remedial training or action. 
                                                    Check (NAR) to reflect narrative comments made in Any category.  
                                                    Check Not Observed (NO) for any area not observed this date. Use the Standardized Evaluation Guidelines (SEG) to determine the trainee performance in each category.
                                            </div>
                                            <br>
                                            <div>
                                                <u>Daily Observation of Trainee</u>
                                                <br>
                                                <br>
                                                You must list specific incidents which demonstrates today’s most and least acceptable areas of performance. 
                                                The most satisfactory area of performance was Rating Category Number: 
                                                <select id="best-category" class="form-select drop-down-categories"></select>
                                                <br>
                                                <textarea class="form-control" id="best-category-text" rows="3"></textarea>
                                            </div>
                                            <br>
                                            <div>
                                                The least satisfactory area of performance today was Rating Category Number: 
                                                <select id="worst-category" class="form-select drop-down-categories"></select>
                                                <br>
                                                <textarea class="form-control" id="worst-category-text" placeholder="Type to enter text..." rows="3"></textarea>
                                            </div>
                                            <br>
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                    <th scope="col" style="width: 25%">Category</th>
                                                    <th scope="col">Documentation of Performance and Comments</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr scope="row">
                                                        <td><select class="form-select drop-down-categories"></select></td>
                                                        <td><textarea class="form-control" id="worst-category-text" placeholder="Type to enter text..." rows="1"></textarea></td>
                                                    </tr>
                                                </tbody>
                                            </table>     
                                             <div class="d-md-flex justify-content-md-end">
                                                <button class="btn btn-secondary" type="button">Add Row</button>
                                            </div>                                       
                                    </div>
                    
                                </div>
                                    
                                </div>
                                <div class="tab-pane fade" id="day-1-plog" role="tabpanel" aria-labelledby="nav-day-1-plog">
                                    <br>
                                    <div class="card shadow">
                                        <div class="card-header d-flex justify-content-center">
                                            <table class="table table-borderless" style ="width: 70%">
                                                <tbody>
                                                    <tr>
                                                        <th>Probationary Deputy</th>
                                                        <td>Test</td>
                                                        <th>Field Training Officer</th>
                                                        <td>
                                                            <select class="form-select">
                                                                    <option>Select</option>
                                                            </select>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th>Date: </th>
                                                        <td>
                                                            <input class="form-control" type="date" value="2019-08-19" id="example-date-input">
                                                        </td>
                                                        <th>DOR #: </th>
                                                        <td>
                                                        <input class="form-control" type="number" value="1" id="example-number-input">
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>                                   
                                        <div class="card-body">
                                            <table class="table table-bordered">
                                                <theader>
                                                    <tr>
                                                        <th>Time Started:</th>
                                                        <th>Time Cleared:</th>
                                                        <th>Location</th>
                                                        <th>Activity</th>
                                                        <th>Disposition</th>
                                                        <th>Primary Contact Deputy</th>                                                    
                                                    </tr>
                                                    <tr>
                                                        <td><input class="form-control" type="time" value="13:45:00" id="example-time-input"></td>
                                                        <td><input class="form-control" type="time" value="13:45:00" id="example-time-input"></td>
                                                        <td><textarea class="form-control" id="worst-category-text" placeholder="Type to enter text..." rows="1"></textarea></td>
                                                        <td><textarea class="form-control" id="worst-category-text" placeholder="Type to enter text..."></textarea></td>
                                                        <td>
                                                            <select class="form-select">
                                                                <option>Select</option>
                                                            </select>
                                                        </td>
                                                        <td>
                                                            <select class="form-select">
                                                                <option>Select</option>
                                                            </select>
                                                        </td>
                                                    </tr>
                                                </theader>
                                            </table>
                                            <div class="d-md-flex justify-content-md-end">
                                                <button class="btn btn-secondary" type="button">Add Row</button>
                                            </div>                                         
                                        </div>                                        
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="day-1-coversheet" role="tabpanel" aria-labelledby="nav-day-1-coversheet">
                                    <br>
                                    <div class="card">
                                        <div class="card-body">
                                            <div class="accordion accordion-flush shadow" id="accordionFlushExample">
                                                <div class="accordion-item">
                                                    <h2 class="accordion-header" id="flush-headingOne">
                                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                                                        Report Cover Sheet
                                                    </button>
                                                    </h2>
                                                    <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
                                                        <div class="accordion-body">
                                                            <div class="d-flex justify-content-center">
                                                                <table class="table table-borderless" style ="width: 70%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <th>Probationary Deputy</th>
                                                                            <td>Test</td>
                                                                            <th>Field Training Officer</th>
                                                                            <td>
                                                                                <select class="form-select">
                                                                                        <option>Select</option>
                                                                                </select>
                                                                            </td>
                                                                        </tr>
                                                                        <tr>
                                                                            <th>Date: </th>
                                                                            <td>
                                                                                <input class="form-control" type="date" value="2019-08-19" id="example-date-input">
                                                                            </td>
                                                                            <th>DOR #: </th>
                                                                            <td>
                                                                            <input class="form-control" type="number" value="1" id="example-number-input">
                                                                            </td>
                                                                        </tr>
                                                                        <tr>
                                                                            <th>Report #:</th>
                                                                            <td><input class="form-control" type="text" placeholder="Type to enter text..." id="example-text-input"></td>
                                                                            <th>Type of Report</th>
                                                                            <td>
                                                                                <select class="form-select">
                                                                                        <option>Select</option>
                                                                                </select>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </div>
                                                            <table class="table">
                                                                <tbody class="questions"></tbody>
                                                            </table>
                                                            <div>
                                                                <textarea class="form-control" id="report-comments" placeholder="Type to enter comments..." rows="3"></textarea>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <br>
                                            <div class="d-md-flex justify-content-md-end">
                                                 <button class="btn btn-secondary" type="button">Add New</button>
                                            </div>                                         
                                        </div>
                                    </div>
                                    
                                
                                </div>
                                <div class="tab-pane fade" id="day-1-misc" role="tabpanel" aria-labelledby="nav-day-1-misc">
                                    <br>


                                    <div class="row ">
                                        <div class="col-12">
                                            <div class="card">
                                                <div class="card-header">
                                                    <h4 class="card-title">Upload any additional items below:</h4>
                                                </div>
                                                <div class="card-body">               
                                                    <div>
                                                        <form action="#" class="dropzone">
                                                            <div class="fallback">
                                                                <input name="file" type="file" multiple="multiple">
                                                            </div>
                                                            <div class="dz-message needsclick">
                                                                <div class="mb-3">
                                                                    <i class="display-4 text-muted bx bx-cloud-upload"></i>
                                                                </div>
                
                                                                <h5>Drop files here or click to upload.</h5>
                                                            </div>
                                                        </form>
                                                    </div>
                
                                                    <div class="text-center mt-4">
                                                        <button type="button" class="btn btn-primary waves-effect waves-light">Send
                                                            Files</button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div> <!-- end col -->
                                    </div> <!-- end row -->
                                </div>
                            </div>`
);

for (var key in categories) {   
    $("#day-1-dor-body").append(
                        `<tr>
                            <th scope="row">${key} <br> ${categories[key]}</th>
                            <td>
                                <select class="form-select">
                                    <option>1</option>
                                    <option>2</option>
                                    <option>3</option>
                                    <option>4</option>
                                    <option>5</option>
                                    <option>6</option>
                                    <option>7</option>
                                    <option>NO</option>
                                    <option>NRT</option>
                                    <option>NAR</option>                                                            
                                </select>
                            </td>
                            <td><input class="form-control" type="number" value="12" id="example-number-input"> Minutes</td>
                        </tr>`
)}

for (var key in categories) {
    $(".drop-down-categories").append(
        `<option>${key}</option>`
    )
}

eval_questions.forEach(element => {
    $(".questions").append(
        `<tr>
            <th>${element}:</th>
            <td>
                <select class="form-select">
                    <option>Select</option>
                    <option>Yes</option>
                    <option>No</option>
                </select>
            </td>
        </tr>`
    )
});

//Weekly Forms
$('#week-modal-body').append(
                 `<nav>
                    <div class="nav nav-tabs" id="nav-tab" role="tablist">
                      <button
                        class="nav-link active"
                        id="nav-sgt-eval"
                        data-bs-toggle="tab"
                        data-bs-target="#sgt-eval"
                        type="button"
                        role="tab"
                        aria-controls="sgt-eval"
                        aria-selected="true"
                      >
                        Sgt. Evaluation
                      </button>
                      <button
                        class="nav-link"
                        id="nav-self-eval"
                        data-bs-toggle="tab"
                        data-bs-target="#self-eval"
                        type="button"
                        role="tab"
                        aria-controls="self-eval"
                        aria-selected="true"
                      >
                        Self Evaluation
                      </button>

                    </div>
                  </nav>
                  <div class="tab-content" id="nav-tabContent">
                    <div
                      class="tab-pane fade show active"
                      id="sgt-eval"
                      role="tabpanel"
                      aria-labelledby="nav-sgt-eval"
                    >
                      <br>
                      <div class="card shadow">
                        <div class="card-body">
                          <div class="d-flex justify-content-center">
                            <table class="table table-borderless" style="width: 80%">
                              <tbody>
                                <tr>
                                  <th>Probationary Deputy</th>
                                  <td>Test</td>
                                  <th>Supervisor</th>
                                  <td>
                                    <select class="form-select">
                                      <option>Select</option>
                                    </select>
                                  </td>
                                </tr>
                                <tr>
                                  <th>Field Training Officer</th>
                                  <td>
                                    <select class="form-select">
                                      <option>Select</option>
                                    </select>
                                  </td>
                                  <th>Date: </th>
                                  <td>
                                    <input class="form-control" type="date" value="2019-08-19" id="example-date-input">
                                  </td>
                                </tr>
                                <tr>
                                  <th>DOR #: </th>
                                  <td>
                                    <div class="form-check form-check-inline">
                                      <input class="form-control" type="number" value="1" id="example-number-input">
                                    </div>
                                    to
                                    <div class="form-check form-check-inline"><input class="form-control" type="number" value="1"
                                        id="example-number-input">
                                    </div>
                                  </td>
                                  <th>Phase</th>
                                  <td>
                                    <select class="form-select">
                                      <option>Select</option>
                                    </select>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                          <br>
                          <div>
                            <h5>Performance and Behavior Observed:</h5>
                            <textarea class="form-control" id="" placeholder="Type to enter text..." rows="2"></textarea>
                            <br>
                            <h5>Training (Current or Suggested):</h5>
                            <textarea class="form-control" id="" placeholder="Type to enter text..." rows="2"></textarea>
                            <br>
                            <h5>Response to PIP or NRT:</h5>
                            <textarea class="form-control" id="" placeholder="Type to enter text..." rows="2"></textarea>
                          </div>
                        </div>
                      </div>

                    </div>

                    <div
                      class="tab-pane fade"
                      id="self-eval"
                      role="tabpanel"
                      aria-labelledby="nav-self-eval"
                    >
                      <br>
                      <div class="card shadow">
                        <div class="card-body">
                          <div class="d-flex justify-content-center">
                            <table class="table table-borderless" style="width: 80%">
                              <tbody>
                                <tr>
                                  <th>Probationary Deputy</th>
                                  <td>Test</td>
                                  <th>Supervisor</th>
                                  <td>
                                    <select class="form-select">
                                      <option>Select</option>
                                    </select>
                                  </td>
                                </tr>
                                <tr>
                                  <th>Field Training Officer</th>
                                  <td>
                                    <select class="form-select">
                                      <option>Select</option>
                                    </select>
                                  </td>
                                  <th>Date: </th>
                                  <td>
                                    <input class="form-control" type="date" value="2019-08-19" id="example-date-input">
                                  </td>
                                </tr>
                                <tr>
                                  <th>DOR #: </th>
                                  <td>
                                    <div class="form-check form-check-inline">
                                      <input class="form-control" type="number" value="1" id="example-number-input">
                                    </div>
                                    to
                                    <div class="form-check form-check-inline"><input class="form-control" type="number" value="1"
                                        id="example-number-input">
                                    </div>
                                  </td>
                                  <th>Phase</th>
                                  <td>
                                    <select class="form-select">
                                      <option>Select</option>
                                    </select>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                          <br>
                          <div>
                            <h6>Instructions:
                              The trainee is to fill out this self-evaluation each week and give to their Supervisor. At the beginning
                              of the next
                              phase they are to fill one out give it to their new FTO
                            </h6>
                            <br>
                            <h5>Trainee Significant Strengths:</h5>
                            <ol>
                              <li><input class="form-control" type="text" placeholder="Enter text..." id=""></li>
                              <li><input class="form-control" type="text" placeholder="Enter text..." id=""></li>
                              <li><input class="form-control" type="text" placeholder="Enter text..." id=""></li>
                            </ol>
                            <br>
                            <h5>Trainee Significant Weaknesses:</h5>
                            <ol>
                              <li><input class="form-control" type="text" placeholder="Enter text..." id=""></li>
                              <li><input class="form-control" type="text" placeholder="Enter text..." id=""></li>
                              <li><input class="form-control" type="text" placeholder="Enter text..." id=""></li>
                            </ol>
                            <br>
                            <h5>Other:</h5>
                            <textarea class="form-control" id="" placeholder="Type to enter text..." rows="2"></textarea>
                          </div>
                        </div>
                      </div>

                    </div>

                  </div>`
)

//Step Evaulation
$("#step-eval-modal-body").append(
    `         <div class="d-flex justify-content-center">
              <table class="table table-borderless" style="width: 80%">
                <tbody>
                  <tr>
                    <th>Probationary Deputy</th>
                    <td>Test</td>
                    <th>Supervisor</th>
                    <td>
                      <select class="form-select">
                        <option>Select</option>
                      </select>
                    </td>
                  </tr>
                  <tr>
                    <th>Field Training Officer</th>
                    <td>
                      <select class="form-select">
                        <option>Select</option>
                      </select>
                    </td>
                    <th>Date: </th>
                    <td>
                      <input class="form-control" type="date" value="2019-08-19" id="example-date-input">
                    </td>
                  </tr>
                  <tr>
                    <th>Phase</th>
                    <td>
                      <select class="form-select">
                        <option>Select</option>
                      </select>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <br>
            <h6>The Probationary Deputy:</h6>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="option-1" id="option-1" value="option1" >
              <label class="form-check-label" for="option-1">
                is progressing satisfactorily
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="option-1" id="option-1" value="option1">
              <label class="form-check-label" for="option-1">
                should advance to the next step/phase
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="option-1" id="option-1" value="option1">
              <label class="form-check-label" for="option-1">
                is experiencing difficulty
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="option-1" id="option-1" value="option1">
              <label class="form-check-label" for="option-1">
                should receive an extension of training
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="option-1" id="option-1" value="option1">
              <label class="form-check-label" for="option-1">
                should be recommended for a Board of Review Hearing
              </label>
            </div>
            <br>
            <h6>Area(s) of strength:</h6>
            <textarea class="form-control" id="" placeholder="Type to enter text..." rows="2"></textarea>
            <br>
            <h6>Area(s) most in need of improvement:</h6>
            <textarea class="form-control" id="" placeholder="Type to enter text..." rows="2"></textarea>
            <br>
            <h6>Additional Comments:</h6>
            <textarea class="form-control" id="" placeholder="Type to enter text..." rows="2"></textarea>
          </div>`
)

//Policies

const policies = {

    "week-1-policies": {
        "1) Establishment of CCSO Directive Manual": [
                            "Lexipol Policy Manual: Policy 103"
        ],
        "2) Mission, Goals & Objectives of CCSO": [
                            "Mission Statement – Lexipol Page 2"
        ],
        "3)	Organizational Structure – Policy 200": [
                            "Field Training Program – Policy 406"
        ],
        "4)	Conduct – Policy 320": ["Conduct – Policy 320"    
        ],
        "5)	Police Operations": ["Sick Leave – Policy 1009", "OT Compensation Request – Policy 1017", "Payroll Record Procedure – Policy 1016", "Shift Scheduling", "Hours of Work",
            "Regular Days Off (RDO’s)", "Outside Employment – Policy 1018", "•	Uniform Regulations – Policy 1021", "•	Personal Appearance Standard – Policy 1020",
            "Department Badges – Policy 1023", "Body Armor – Policy 1004", "Communicable Diseases – Policy 1011", "Occupational Diseases & Work Related Injuries – Policy 1019"         
        ],
        "6)	Use of Force – Policy 300": [ "Use of Force – Policy 300"   
        ],
        "7)	Service Weapons – Policy 303": ["720 ILCS 5/7-5 (Peace Officer’s Use of Force in Making Arrest)", "720 ILCS 5/7-8 (Force Causing Death of Great Bodily Harm)", "720 ILCS 5/7-9 (Use of Force to Prevent Escape)",
            "725 ILCS 5/107-2 (Arrest by Peace Officer) – Requirements by law in regards to dependent children – Defines arrest by Peace Officer including “Good Faith Arrest” and Arrest Warrant",
            "725 ILCS 5/107-5 (Method of Arrest)", "725 ILCS 5/107-6 (Released by Officer of Person Arrested)", "725 ILCS 5/107-12 (Notice to Appear)",
            "725 ILCS 5/107-14 (Temporary Questioning without Arrest)", "725 ILCS 5/108-1(Search Without Warrant)", "725 ILCS 5/108-1.01 (Search During Temporary Questioning)",
            "725ILCS5/107-6 (Released by Officer of Person Arrested)"
        ],
        "8)	Search & Seizures – Policy 323": ["Search & Seizures – Policy 323"
        ],
        "9)	Handcuffing/Restraint – Policy 301": [ "Handcuffing/Restraint – Policy 301"
            
        ],
        "10) Custodial Searches – Policy 900": ["Custodial Searches – Policy 900"
            
        ],
        "11) Portable Audio/Video Recorders – Policy 408": ["Portable Audio/Video Recorders – Policy 408"
            
        ],
        "12) Conduct & Responsibilities On Duty & Off Duty – Policy 320": ["Conduct & Responsibilities On Duty & Off Duty – Policy 320"
            
        ],
        "13) Familiarization with County Facilities & Services": ["Sheriff’s Office/Satellite Jail", "Courthouse (SAO, Probation, Public Defender, Central)", "Juvenile Detention Center", "Coroner’s Office",
            "Brookens Administrative Center", "County Highway", "Sheriff’s Garage/Impound Lot", "METCAD", "Champaign County Nursing Home"
        ],
        "14) Familiarization with Other Police Agencies": ["Urbana Police Department", "U of I Police Department", "Champaign Police Department", "Rantoul Police Department", "Mahomet Police Department", "Fisher Police Department",
            "Fisher Police Department", "Ludlow Police Department", "Gifford Police Department", "Thomasboro Police Department", "Homer Police Department", "Illinois State Police, Pesotum",
            "ISP Zone 5 Investigations", "IDOC Parole Office" 
        ],
        "15) Familiarization with Local Service Providers:": ["Carle Foundation Hospital", "OSF Hospital", "Community Elements", "Rosecrance"
        ],
        "16) Services to Juveniles": ["Juvenile Detention Center","Youth Assessment Center"           
        ],
        "17) Substance Abuse": ["Prairie Center", "Carle Hospital", "The Pavilion "
        ],
        "18) Sexual Assault Victim ": ["Sexual Assault Victim – Policy 607", "Rape Crisis Center", "A Women’s Fund"
        ],
        "19) Emergency Shelters:": ["Times Center", "Salvation Army", "Catholic Workers House (women & children)"
        ],
        "20) Police Radio System": ["Mobile Data Computer – Policy 407", "Operation and Knowledge of the Police Radio System", "Maintenance of Radios"           
        ],       
        "21) Sheriff’s Vehicle Operations": ["Vehicle Use – Policy 702", "Vehicle Maintenance – Policy 703", "Response to Calls – Policy 324", "Vehicle Pursuits – Policy 325]",
            "Traffic Crashes Involving County Vehicles – Policy 501.3.1"    
        ],
        "22) Orientation Skills": ["Computer Use – Policy 203", "Information Technology Use – Policy 332"
            
        ]                        
    },
    "week-2-policies": {
        
    }






}

$("#policies-modal-body").append(
            `  <nav>
                <div class="nav nav-tabs" id="nav-tab" role="tablist">
                  <button class="nav-link active" id="nav-policies-week1" data-bs-toggle="tab" data-bs-target="#policies-week1" type="button"
                    role="tab" aria-controls="policies-week1" aria-selected="true">
                    Week #1
                  </button>
                  <button class="nav-link" id="nav-policies-week2" data-bs-toggle="tab" data-bs-target="#policies-week2" type="button"
                    role="tab" aria-controls="policies-week2" aria-selected="true">
                    Week #2
                  </button>
              
                </div>
              </nav>

              <div class="tab-content " id="nav-tabContent">
                <div class="tab-pane fade show active" id="policies-week1" role="tabpanel" aria-labelledby="nav-policies-week1">
                  <br>
                    <table class="table table-bordered text-center policies-table "></table>
                </div>
                <div class="tab-pane fade" id="policies-week2" role="tabpanel" aria-labelledby="nav-policies-week2">
                  d
                </div>
              </div>
        </div>
      </div>
              
              `

)

$('.policies-table').append(
            `<thead>
                <th style="width: 40%;">Policy</th>
                <th>Instructed by FTO</th>
                <th>Demonstrated by FTO</th>
                <th>Task/Knowledge Proficiency Demonstrated by PD</th>
            </thead>
            <tbody class="policies-table-body "></tbody>`
)


for (var category in policies["week-1-policies"]) {
    $('.policies-table-body').append(
        `<tr>
            <th colspan="4">
            ${category}
            </th>
        </tr>`
    )

    policies["week-1-policies"][category].forEach(policy => {          
        $(".policies-table-body").append(
            `<tr>
                <td>
                    ${policy}
                </td>
                <td>
                    <input class="form-check-input" type="checkbox" id="">
                </td>
                <td>
                    <input class="form-check-input" type="checkbox" id="">
                </td>
                <td>
                    <input class="form-check-input" type="checkbox" id="">
                </td>
            </tr>`
        )        
    })
}

//Resources

$("#recruit-resources-modal-body").append(
          `<a href="#" data-bs-toggle="collapse" data-bs-target="#beats-location">City/Village Beats</a>
            <div id="beats-location" class="collapse">
              <pre>
                City/Village Beats                  Township Beats - Location
                1 Champaign                         50 Brown 3000N-3600E & 000E-600E
                2 Urbana                            51 East Bend 3000N-3600N & 600E-1200E
                3 University of Illinois            52 Ludlow 3000N-3600N & 1200E-1800E
                4 Foosland                          53 Harwood 3000N-3600N & 1800E-2400E
                5 Fisher                            54 Kerr 3000N-3600N & 2400E-2800E
                6 Ludlow                            55 Newcomb 2400N-3000N & 000E-600E
                7 Gifford                           56 Condit 2400N-3000N & 600E-1200E
                8 Thomasboro                        57 Rantoul 2400N-3000N & 1200E-2000E
                9 Bondville                         58 Compromise 2400N-3000N & 2000E-2800E
                10 Savoy                            59 Mahomet 1800N-2400N & 000E-600E
                11 Saint Joseph                     60 Hensley 1800N-2400N & 600E-1200E
                12 Royal                            61 Somer 1800N-2400N & 1200E-1800E
                13 Ogden                            62 Stanton 1800N-2400N & 1800E-2400E
                14 Ivesdale                         63 Ogden 1350N-2400N & 2400E-2800E
                15 Sadorus                          64 Scott 1200N-1800N & 000E-600E
                16 Pesotum                          65 Champaign 1200N-1800N & 600E-1200E
                17 Philo                            66 Urbana 1200N-1800N & 1200E-1800E
                18 Sidney                           67 St. Joseph 1200N-1800N & 1800E-2400E
                19 Homer                            68 Colfax 600N-1200N & 000E-600E
                20 Longview                         69 Tolono 600N-1200N & 600E-1200E
                21 Broadlands                       70 Philo 600N-1200N & 1200E-1800E
                22 Mahomet                          71 Sidney 600N-1200N & 1800E-2400E
                23 Rantoul                          72 South Homer 600N-1350N & 2400E-2800E
                24 Tolono                           73 Sadorus 000N-600N & 000E-600E
                30 Lotus                            74 Pesotum 000N-600N & 600E-1200E
                31 Dewey                            75 Crittenden 000N-600N & 1200E-1800E
                32 Penfield                         76 Raymond 000N-600N & 1800E-2400E
                33 Seymour                          77 Ayers 000N-600N & 2400E-2800E
                                                    80 Forest Preserves Lake of the Woods, Homer, Penfield
              </pre>
            </div>
            <br><br>
            <a href="#" data-bs-toggle="collapse" data-bs-target="#ten-codes">10-Codes</a>
            <div id="ten-codes" class="collapse">
              <pre>
                10-0 – Caution                              10-40 – Silent Run-no light/siren       10-86 – Officer/Operator on Duty
                10-1 – Unable to Copy                       10-41 – Beginning Tour of Duty          10-87 – Pickup/Distribute Checks
                10-2 – Signal Good                          10-42 – Ending Tour of Duty             10-88 – Present Telephone # of…
                10-3 – Stop Transmitting                    10-43 - Information                     10-89 – Bomb Threat
                10-4 – Acknowledged (OK)                    10-44 – Permission to Leave….for        10-90 – Bank Alarm at…
                10-5 – Relay                                10-45 – Animal Carcass at…              10-91 – Pickup Prisoner/Subject
                10-6 – Busy-unless urgent                   10-46 – Assist Motorist                 10-92 – Improperly Parked Vehicle
                10-7 – Out of Service                       10-47 – Emergency Road Repair at…       10-93 – Blockade
                10-8 – In Service                           10-48 – Traffic Standard Repair at…     10-94 – Drag Racing
                10-9 – Repeat                               10-49 – Traffic Light Out at…           10-95 – Prisoner/Subject in Custody
                10-10 – Fight in Progress                   10-50 – Accident (PI, PD)               10-96 – Mental Subject
                10-11 – Dog Case                            10-51 – Wrecker Needed                  10-97 – Check (test) Signal
                10-12 – Standby (Stop)                      10-52 – Ambulance Needed                10-98 – Prison/Jail Break
                10-13 – Weather/Road Report                 10-53 – Road Blocked at…                10-99 – Wanted/Stolen Indicated
                10-14 – Prowler Report                      10-54 – Livestock on Highway
                10-15 – Civil Disturbance                   10-55 – Intoxicated Driver
                10-16 – Domestic Problem                    10-56 – Intoxicated Pedestrian
                10-17 – Meet Complainant                    10-57 – Hit and Run (PD, PD)
                10-18 – Quickly                             10-58 – Direct Traffic
                10-19 – Return to…                          10-59 – Convoy or Escort
                10-20 – Location                            10-60 – Squad in Vicinity
                10-21 – Call – By Telephone                 10-61 – Personnel in Area
                10-22 – Disregard/Cancel                    10-62 – Reply to Message
                10-23 – Arrived at Scene                    10-63 – Prepare/Make Written Copy
                10-24 – Assignment Completed                10-64 – Message for Local Delivery
                10-25 – Report in Person (meet)             10-65 – Net Message Assignment
                10-26 – Detaining Subject, Expedite         10-66 – Message Cancellation
                10-27 – Driver’s License Information        10-67 – Clear for Net Message
                10-28 – Vehicle Reg. Information            10-68 – Dispatch Information
                10-29 – Check for Wanted                    10-69 – Message Received
                10-30 – Unnecessary Use of Radio            10-70 – Fire Alarm
                10-31 – Crime in Progress                   10-80 – Chase in Progress
                10-32 – Man with Gun                        10-81 – Breathalyzer Report
                10-33 – EMERGENCY                           10-82 – Reserve Lodging
                10-34 – Riot                                10-83 – Work School Crossing at…
                10-35 – Major Crime Alert                   10-84 – If Meeting, advise ETA…
                10-36 – Correct Time                        10-85 – Delayed Due to….
                10-37 – (Investigate) Suspicious Vehicle
                10-38 – Stopping Suspicious Vehicle
                10-39 – Urgent-use light/siren
              </pre>
            </div>
            <br><br>
            <a href="#" data-bs-toggle="collapse" data-bs-target="#activity-codes">Activity Codes</a>
            <div id="activity-codes" class="collapse">
              <pre>
                Code 1 – Officer Needs Help (EMERGENCY)     Code 38 – Traffic Stop
                Code 4 – Officer Okay Code                  39 – Accident Investigation
                Code 5 – Surveillance Code                  41 – Training
                Code 20 – Unassigned Patrol Code            42 – Public Relations
                Code 21 – Mobil Patrol (One Officer) Code   44 – Personal Time/Lunch
                Code 22 – Mobil Patrol (Two Officers) Code  45- Desk Duty
                Code 23 – Unmarked Patrol Code              46 – Shift Supervisor
                Code 24 – Foot Patrol Code                  48 – Equipment/Vehicle Maintenance
                Code 25 – Special patrol Code               49 – Court Duty
                Code 27 – Follow-up Code                    50 – Report Writing
                Code 28 – Miscellaneous Investigation Code  51 – Building Check
                Code 29 – Arrest Activity Code              52 – Miscellaneous Activity
                Code 34 – Parking Enforcement Code          53 – Service Delivery
                Code 36 – Traffic Enforcement/Radar Code    55 – Flag Detail
                Code 59 – Escort
                Code 200 – Fuel Conservation

              </pre>
            </div>`
)
