var data = [
  {
    x: ["-35.3", "-15.9", "-15.8", "-15.6", "-11.1", "-9.6", "-9.2", "-3.5", "-1.9", "-0.9", "1.0", "1.4", "1.7", "2.0", "2.8", "6.2", "8.1", "8.5", "8.5", "8.6", "11.4", "12.5", "13.3", "13.7", "14.4", "17.5", "17.7", "18.9", "25.1", "28.9", "41.4"],
    y: ["Designers, musicians, artists, etc.", "Secretaries and administrative assistants", "Waiters and servers", "Archivists, curators, and librarians", "Sales and related", "Childcare workers, home car workers, etc.", "Food preparation occupations", "Janitors, maids, etc.", "Healthcare technicians, assistants. and aides", "Counselors, social and religious workers", "Physical, life and social scientists", "Construction", "Factory assembly workers", "Machinists, repairmen, etc.", "Media and communications workers", "Teachers", "Mechanics, repairmen, etc.", "Financial analysts and advisers", "Farming, fishing and forestry workers", "Truck drivers, heavy equipment operator, etc.", "Accountants and auditors", "Human resources, management analysts, etc.", "Managers", "Lawyers and judges", "Engineers, architects and surveyors", "Nurses", "Legal support workers", "Computer programmers and system admin.", "Police officers and firefighters", "Chief executives", "Doctors, dentists and surgeons"],
    marker: {
      color: "rgb(253, 240, 54)",
      line: {
        color: "rgb(0, 0, 0)",
        width: 2
      }
    },
    name: "y",
    orientation: "h",
    type: "bar",
  }
];
var layout = {
  autosize: false,
  bargap: 0.15,
  bargroupgap: 0.1,
  barmode: "stack",
  height: 800,
  hovermode: "x",
  images: [
    {
      x: 1,
      y: 1.05,
      sizex: 0.2,
      sizey: 0.2,
      source: "https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/vox.png",
      xanchor: "right",
      xref: "paper",
      yanchor: "bottom",
      yref: "paper"
    }
  ],
  margin: {
    r: 20,
    t: 125,
    b: 75,
    l: 300
  },
  title: "Moving Up, Moving Down. Percentile change in income between childhood and adulthood",
  width: 700,
  xaxis: {
    autotick: false,
    dtick: 10,
    gridcolor: "rgba(102, 102, 102, 0.4)",
    linecolor: "#000",
    linewidth: 1,
    mirror: true,
    nticks: 0,
    showticklabels: true,
    tick0: 0,
    tickwidth: 1,
    title: "Change in percentile"
  },
  yaxis: {
    anchor: "x",
    autotick: false,
    gridcolor: "rgba(102, 102, 102, 0.4)",
    gridwidth: 1,
    linecolor: "#000",
    linewidth: 1,
    mirror: true,
    showgrid: false,
    showline: true,
    showticklabels: true,
    tick0: 0,
    type: "category",
    zeroline: false
  }
};

Plotly.plot('plotly-div', data, layout);