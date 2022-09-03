//DOR categories
const categories = {
    "1. Appearance": "Physical appearance, dress, and demeanor.",
    "2.Attitude": "Interaction between Probationary Officer and FTO, Probationary Officer and individuals in the community.",
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
                        
$("#day-1-modal").append(
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