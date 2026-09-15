import { useState, useEffect } from "react";
import "./App.css";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Legend,
} from "recharts";

function App() {
  const [developers, setDevelopers] = useState([]);
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/developers")
      .then((res) => res.json())
      .then((result) => setDevelopers(result))
      .catch((err) => console.log(err));

    fetch("http://127.0.0.1:8000/commits")
      .then((res) => res.json())
      .then((result) => setData(result))
      .catch((err) => console.log(err));
  }, []);

  const pieData = [
    { name: "Focused", value: 70 },
    { name: "Meetings", value: 20 },
    { name: "Break", value: 10 },
  ];

  const COLORS = ["#0d6efd", "#198754", "#ffc107"];

  return (
    <div className="container mt-4">
      <nav className="navbar navbar-dark bg-dark rounded mb-4">
        <div className="container-fluid">
          <span className="navbar-brand">CogniStream Analytics</span>
        </div>
      </nav>

      <h1 className="text-center text-primary mb-4">
        CogniStream Dashboard
      </h1>

      <div className="row">
        <div className="col-md-3">
          <div className="card shadow text-center p-3">
            <h5>Total Developers</h5>
            <h2>{developers.length}</h2>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card shadow text-center p-3">
            <h5>Commits Today</h5>
            <h2>180</h2>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card shadow text-center p-3">
            <h5>PRs Open</h5>
            <h2>14</h2>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card shadow text-center p-3">
            <h5>Focus Score</h5>
            <h2>92%</h2>
          </div>
        </div>
      </div>

      <div className="card shadow p-3 mt-4">
        <h4>Weekly Commits</h4>

        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <XAxis dataKey="day" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="commits" fill="#0d6efd" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="card shadow p-3 mt-4">
        <h4>Developer Activity</h4>

        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={pieData}
              dataKey="value"
              nameKey="name"
              outerRadius={100}
              label
            >
              {pieData.map((entry, index) => (
                <Cell
                  key={index}
                  fill={COLORS[index % COLORS.length]}
                />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </div>

      <div className="card shadow mt-4">
        <div className="card-header bg-primary text-white">
          Recent Activity
        </div>

        <div className="card-body">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Developer</th>
                <th>Project</th>
                <th>Status</th>
                <th>Last Commit</th>
              </tr>
            </thead>

            <tbody>
              {developers.map((dev, index) => (
                <tr key={index}>
                  <td>{dev.name}</td>
                  <td>{dev.project}</td>
                  <td>{dev.status}</td>
                  <td>{dev.last_commit}</td>
                </tr>
              ))}
            </tbody>

          </table>
        </div>
      </div>
    </div>
  );
}

export default App;