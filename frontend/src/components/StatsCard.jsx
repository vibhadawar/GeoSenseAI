function StatsCard({ stats }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <h2 className="text-2xl font-bold mb-6">
        Land Cover Statistics
      </h2>

      <div className="space-y-5">

        <div>
          <div className="flex justify-between mb-1">
            <span>🟩 Vegetation</span>
            <span>{stats.vegetation_percent}%</span>
          </div>

          <div className="w-full bg-gray-200 rounded-full h-3">
            <div
              className="bg-green-500 h-3 rounded-full"
              style={{
                width: `${stats.vegetation_percent}%`,
              }}
            ></div>
          </div>
        </div>

        <div>
          <div className="flex justify-between mb-1">
            <span>🟦 Water</span>
            <span>{stats.water_percent}%</span>
          </div>

          <div className="w-full bg-gray-200 rounded-full h-3">
            <div
              className="bg-blue-500 h-3 rounded-full"
              style={{
                width: `${stats.water_percent}%`,
              }}
            ></div>
          </div>
        </div>

        <div>
          <div className="flex justify-between mb-1">
            <span>⬜ Urban</span>
            <span>{stats.urban_percent}%</span>
          </div>

          <div className="w-full bg-gray-200 rounded-full h-3">
            <div
              className="bg-gray-500 h-3 rounded-full"
              style={{
                width: `${stats.urban_percent}%`,
              }}
            ></div>
          </div>
        </div>

      </div>

    </div>
  );
}

export default StatsCard;