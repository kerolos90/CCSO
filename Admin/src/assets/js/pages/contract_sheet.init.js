//Monthly Totals
$("#monthly_totals").append(
                            `<h3 class="text-center">Monthly Totals:</h3>
                            <table class="table">
                                <thead>
                                <tr>
                                    <th colspan="2" scope="col">Value</th>
                                    <th colspan="2" scope="col">Totals</th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr>
                                    <th colspan="2" scope="row">Miles:</th>
                                    <td colspan="2">300</td>
                                </tr>
                                <tr>
                                    <th scope="row">Traffic Stops:</th>
                                    <td colspan="2">25</td>
                                </tr>
                                <tr>
                                    <th scope="row">Papers Served:</th>
                                    <td colspan="2">3</td>
                                </tr>
                                </tbody>
                            </table>`
);


// Contract Sheet Modal

const activities = ["Car Patrol", "Foot Patrol", "Report Writing", "Court", "Traffic Detail", "Special Detail", "Crash Inv.", "Criminal Inv.", "Other Inv."];
const productivity = ["Traffic Arrests", "Criminal Arrests", "Written Warnings", "Accidents Inv.", "    a. Vehicles Involved", "     b. Injuries", , "     c. Fatalities", "Papers Served"];
var title = $("#village_title").text();

$("#contract_sheet_modal").append(
                                `<div class="modal-header py-3 px-4 border-bottom-0">
                                <button
                                    type="button"
                                    class="btn-close"
                                    data-bs-dismiss="modal"
                                    aria-hidden="true"
                                ></button>
                                </div>
                                <div class="modal-body p-4">
                                <div class="card">
                                    <h1 class="card-title text-center fs-5">
                                    Champaign County Sherrif's Office
                                    </h1>
                                    <h2
                                    class="card-subtitle mb-2 text-muted text-center fs-6"
                                    >
                                    Village of ${title}
                                    <br /><br />
                                    Contractual Police Services
                                    <br />
                                    Daily Activity Report
                                    </h2>
                                    <div class="card-body" style="font-size: 0.9em">
                                    <div class="table-responsive">
                                        <table
                                        class="table table-bordered"
                                        style="font-size: inherit"
                                        >
                                        <tbody>
                                            <tr>
                                            <th>Date:</th>
                                            <td>
                                                <input
                                                class="form-control"
                                                type="date"
                                                value="2019-08-19"
                                                id="example-date-input"
                                                />
                                            </td>
                                            <th>Deputy</th>
                                            <td>
                                                <input
                                                class="form-control"
                                                list="datalistOptions"
                                                id="exampleDataList"
                                                placeholder="Type to search..."
                                                />
                                            </td>
                                            <th>Car#:</th>
                                            <td>
                                                <input
                                                class="form-control"
                                                type="number"
                                                value="1"
                                                id="example-number-input"
                                                />
                                            </td>
                                            </tr>
                                            <tr>
                                            <th>Miles:</th>
                                            <td>
                                                <input
                                                class="form-control"
                                                type="number"
                                                value="1"
                                                id="example-number-input"
                                                />
                                                <input
                                                class="form-control"
                                                type="number"
                                                value="1"
                                                id="example-number-input"
                                                />
                                            </td>
                                            <td>Time Start:</td>
                                            <td>
                                                <input
                                                class="form-control"
                                                type="time"
                                                value="13:45:00"
                                                id="example-time-input"
                                                />
                                                <input
                                                class="form-control"
                                                type="time"
                                                value="14:45:00"
                                                id="example-time-input"
                                                />
                                            </td>
                                            <th>Weather:</th>
                                            <td>
                                                <select class="form-select">
                                                <option>Select</option>
                                                <option>Clear</option>
                                                <option>Rain</option>
                                                <option>Snow</option>
                                                </select>
                                            </td>
                                            </tr>
                                            <tr>
                                            <th>Total Miles:</th>
                                            <td>5 miles</td>
                                            <th>Total Time:</th>
                                            <td>1 Hour</td>
                                            </tr>
                                        </tbody>
                                        </table>
                                    </div>
                                    <br />
                                    <div class="table-responsive">
                                        <table
                                        class="table table-bordered"
                                        id="activity_table"
                                        style="font-size: inherit"
                                        >
                                        <thead>
                                            <tr>
                                            <th scope="col" style="width: 15%">
                                                Activity
                                            </th>
                                            <th
                                                colspan="2"
                                                style="width: 10%"
                                                scope="col"
                                            >
                                                Time Spent
                                            </th>
                                            <th scope="col">Activity Log</th>
                                            </tr>
                                        </thead>
                                        <tbody></tbody>
                                        </table>
                                        <table
                                        class="table table-bordered"
                                        id="productivity_table"
                                        style="font-size: inherit"
                                        >
                                        <thead>
                                            <tr>
                                            <th scope="col">Productivity</th>
                                            <th scope="col">Numbers</th>
                                            <th style="width: 70%" scope="col">
                                                Activity Log
                                            </th>
                                            </tr>
                                        </thead>
                                        <tbody></tbody>
                                        </table>
                                        <div class="container-fluid text-end">
                                        Submitted by: Deputy Gabra #503
                                        </div>
                                    </div>
                                    </div>
                                </div>
                                <!--Submit and Cancel buttons  -->
                                <div class="row mt-2">
                                    <div class="col-6">
                                    <button
                                        type="button"
                                        class="btn btn-danger"
                                        id="btn-delete-event"
                                    >
                                        Cancel
                                    </button>
                                    </div>
                                    <div class="col-6 text-end">
                                    <button
                                        type="submit"
                                        class="btn btn-success"
                                        id="btn-save-event"
                                    >
                                        Submit
                                    </button>
                                    </div>
                                </div>
                                </div>`
)

activities.forEach(element => {
    $("#activity_table").append(`   <tr>
                                        <th scope="row">${element}</th>
                                        <td style="width: 10%;" >
                                            <input
                                            class="form-control"
                                            type="number"
                                            value="0"
                                            id="example-number-input"
                                            />
                                            Hour(s)
                                        </td>
                                        <td>
                                            <select class="form-select">
                                                <option>0</option>
                                                <option>15</option>
                                                <option>30</option>
                                                <option>45</option>
                                                </select>
                                            Minutes
                                        </td>
                                        <td>
                                            <input class="form-control" type="text" placeholder="Enter text..." id="example-text-input">
                                        </td>                                      
                                    </tr>
                                    `)
});

$("#activity_table").append(
                            `<th style="line-height:155%"scope="row">Total Time Spent</th>
                            <td colspan="3">1 Hour 15 Minutes</td>`
)

productivity.forEach(element => {
    $("#productivity_table").append(`   <tr>
                                        <th scope="row">${element}</th>
                                        <td >
                                            <input
                                            class="form-control"
                                            type="number"
                                            value="0"
                                            id="example-number-input"
                                            />
                                        </td>
                                        <td>
                                            <input class="form-control" type="text" placeholder="Enter text..." id="example-text-input">
                                        </td>                                      
                                    </tr>
    `)
});