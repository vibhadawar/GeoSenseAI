import {
  Upload,
  Scan,
  Trees,
  FileText,
  PieChart,
  Search
} from "lucide-react";

const features = [
  {
    icon: Upload,
    title: "Image Upload",
    desc: "Upload satellite imagery for analysis"
  },
  {
    icon: Scan,
    title: "Segmentation",
    desc: "Detect vegetation, water and urban areas"
  },
  {
    icon: Trees,
    title: "Land Cover",
    desc: "Analyze environmental composition"
  },
  {
    icon: PieChart,
    title: "Visual Insights",
    desc: "Interactive statistics and charts"
  },
  {
    icon: FileText,
    title: "AI Reports",
    desc: "Generate environmental summaries"
  },
  {
    icon: Search,
    title: "Change Detection",
    desc: "Compare images over time"
  }
];

function Features() {
  return (
    <section id="features" className="py-24 bg-slate-50">
      <div className="max-w-7xl mx-auto px-6">

        <h2 className="text-4xl font-bold text-center mb-12">
          Powerful Features
        </h2>

        <div className="grid md:grid-cols-3 gap-8">

          {features.map((feature, index) => {
            const Icon = feature.icon;

            return (
              <div
                key={index}
                className="bg-white p-6 rounded-2xl shadow-lg hover:-translate-y-2 transition"
              >
                <Icon size={40} />

                <h3 className="text-xl font-semibold mt-4">
                  {feature.title}
                </h3>

                <p className="text-gray-600 mt-2">
                  {feature.desc}
                </p>
              </div>
            );
          })}

        </div>

      </div>
    </section>
  );
}

export default Features;