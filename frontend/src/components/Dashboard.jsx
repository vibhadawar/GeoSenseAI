import { useState } from "react";

import UploadBox from "./UploadBox";
import StatsCard from "./StatsCard";
import PieChartComponent from "./piechart";
import ImageDisplay from "./imagedisplay";
import ReportCard from "./ReportCard";

function Dashboard() {
  const [stats, setStats] = useState({
    vegetation_percent: 0,
    water_percent: 0,
    urban_percent: 0,
  });

  const [report, setReport] = useState("");

  return (
    <section
      id="analysis"
      className="py-20 px-6"
    >
      <div className="max-w-7xl mx-auto">

        <h2 className="text-4xl font-bold text-center mb-12">
          Analysis Dashboard
        </h2>

        <UploadBox
          setStats={setStats}
          setReport={setReport}
        />

        <div className="grid lg:grid-cols-2 gap-6 mt-8">

          <StatsCard stats={stats} />

          <PieChartComponent stats={stats} />

        </div>

        <div className="mt-8">
          <ImageDisplay />
        </div>

        <div className="mt-8">
          <ReportCard report={report} />
        </div>

      </div>
    </section>
  );
}

export default Dashboard;