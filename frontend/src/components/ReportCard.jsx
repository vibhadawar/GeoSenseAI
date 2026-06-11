function ReportCard({ report }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <h2 className="text-2xl font-bold mb-4">
        AI Environmental Report
      </h2>

      <p className="text-gray-700 leading-8">
        {report || "Upload an image to generate a report."}
      </p>

    </div>
  );
}

export default ReportCard;