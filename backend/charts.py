import matplotlib.pyplot as plt

def create_pie_chart(vegetation, water, urban):

    labels = ["Vegetation", "Water", "Urban"]
    sizes = [vegetation, water, urban]

    plt.figure(figsize=(6,6))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Land Cover Distribution")

    plt.savefig("outputs/pie_chart.png")

    plt.close()