import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_style("whitegrid")

def kpi_card(title, value, emoji="📊"):
    st.metric(label=f"{emoji} {title}", value=value)


def bar_chart(data, title, xlabel="", ylabel=""):
    fig, ax = plt.subplots()
    data.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)


def sustainability_radar(scores_dict):
    labels = list(scores_dict.keys())
    values = list(scores_dict.values())
    values += values[:1]

    angles = [n / float(len(labels)) * 2 * 3.14 for n in range(len(labels))]
    angles += angles[:1]

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids([a * 180 / 3.14 for a in angles[:-1]], labels)
    ax.set_title("🌍 Sustainability Radar Chart")

    st.pyplot(fig)
