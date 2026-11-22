import React, { useState } from "react";
import StudentArray from "./data";

function App() {
  const [studentList, setStudentList] = useState(StudentArray);
  const [branchList] = useState(["CS", "IT", "CV", "MECH"]);
  const [branchFilter, setBranchFilter] = useState("All");

  const addStudent = () => {
    let roll = document.getElementById("rollno").value;
    let name = document.getElementById("name").value;
    let gender = document.getElementById("gender").value;
    let branch = document.getElementById("branch").value;

    let newStudent = { roll, name, gender, branch };

    
    setStudentList([...studentList, newStudent]);
  };

  return (
    <>
      <div className="bg-primary p-1">
        <h5 className="text-white text-center">Student App</h5>
      </div>

      <div className="container mt-3 mb-3">
        <div className="row">
          <div className="col-md-6">
            <input id="rollno" type="text" placeholder="Enter student roll number" className="form-control" />
          </div>
          <div className="col-md-6">
            <input id="name" type="text" placeholder="Enter student name" className="form-control" />
          </div>
        </div>

        <div className="row mt-2">
          <div className="col-md-6">
            <select id="branch" className="form-control">
              <option>Select branch</option>
              {branchList.map((branch) => (
                <option key={branch}>{branch}</option>
              ))}
            </select>
          </div>

          <div className="col-md-6">
            <select id="gender" className="form-control">
              <option>Select gender</option>
              <option>Male</option>
              <option>Female</option>
            </select>
          </div>
        </div>

        <div className="row mt-2">
          <div className="col-md-6">
            <button onClick={addStudent} className="btn btn-success">ADD</button>
          </div>

          <div className="col-md-6">
            <button onClick={() => setBranchFilter("CS")} className="ml-2 btn btn-info">
              CS({studentList.filter((s) => s.branch === "CS").length})
            </button>

            <button onClick={() => setBranchFilter("IT")} className="ml-2 btn btn-danger">
              IT({studentList.filter((s) => s.branch === "IT").length})
            </button>

            <button onClick={() => setBranchFilter("CV")} className="ml-2 btn btn-primary">
              CV({studentList.filter((s) => s.branch === "CV").length})
            </button>

            <button onClick={() => setBranchFilter("MECH")} className="ml-2 btn btn-warning">
              MECH({studentList.filter((s) => s.branch === "MECH").length})
            </button>

            <button onClick={() => setBranchFilter("All")} className="ml-2 btn btn-secondary">
              Total({studentList.length})
            </button>
          </div>
        </div>
      </div>

      <table className="table table-striped">
        <thead>
          <tr>
            <th>S.no</th>
            <th>Roll number</th>
            <th>Name</th>
            <th>Gender</th>
            <th>Branch</th>
            <th>Remove</th>
          </tr>
        </thead>

        <tbody>
          {studentList
            .filter(
              (student) =>
                branchFilter === "All" ||
                student.branch === branchFilter
            )
            .map((student, index) => (
              <tr key={index}>
                <td>{index + 1}</td>
                <td>{student.roll}</td>
                <td>{student.name}</td>
                <td>{student.gender}</td>
                <td>{student.branch}</td>
                <td>
                  <button className="btn btn-outline-danger">Remove</button>
                </td>
              </tr>
            ))}
        </tbody>
      </table>
    </>
  );
}

export default App;