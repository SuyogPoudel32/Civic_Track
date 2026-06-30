function show_time() {
    const live_timestamp = document.getElementById("live-timestamp");
    const date = new Date();
    live_timestamp.innerHTML = `<i class="fa-solid fa-circle text-emerald-400 animate-pulse text-[8px] mr-1.5"></i> Live Monitor: ${date.toLocaleDateString()} | ${date.toLocaleTimeString()}`
}
setInterval(() => {
    show_time()
}, 1000);

function setActiveTimeline(category, location, status) {
    console.log(category, location, status);
    const active_case_name = document.getElementById("active-case-name");
    active_case_name.innerText = category
    const stepReported = document.getElementById("step-reported");
    const stepViewed = document.getElementById("step-viewed");
    const stepWorking = document.getElementById("step-working");
    const stepResolved = document.getElementById("step-resolved");

    

    [stepReported, stepViewed, stepWorking, stepResolved].forEach(element => {
        element.className = "flex-1 bg-[#111c2e] text-slate-500 border border-slate-800 rounded-xl p-4 flex flex-col items-center justify-center text-center space-y-1 shadow-md transition-all"
    });
    if (status == "In Progress") {
        stepReported.className = "flex-1 bg-sky-500/10 text-sky-400 border border-sky-500/40 rounded-xl p-4 flex flex-col items-center justify-center text-center space-y-1 shadow-lg ring-1 ring-sky-500/30 scale-105 font-bold";
        stepViewed.className = "flex-1 bg-sky-500/10 text-sky-400 border border-sky-500/40 rounded-xl p-4 flex flex-col items-center justify-center text-center space-y-1 shadow-lg ring-1 ring-sky-500/30 scale-105 font-bold";
        stepWorking.className = "flex-1 bg-amber-500/10 text-amber-400 border border-amber-500/40 rounded-xl p-4 flex flex-col items-center justify-center text-center space-y-1 shadow-lg ring-1 ring-amber-500/30 scale-105 font-bold animate-pulse";
        return;
    }
    else if (status == "Under Review") {
        stepReported.className = "flex-1 bg-sky-500/10 text-sky-400 border border-sky-500/40 rounded-xl p-4 flex flex-col items-center justify-center text-center space-y-1 shadow-md";
        stepViewed.className = "flex-1 bg-amber-500/10 text-amber-400 border border-amber-500/40 rounded-xl p-4 flex flex-col items-center justify-center text-center space-y-1 shadow-lg scale-105 font-bold";
        return;
    }
    else if (status === 'Resolved') {
        [stepReported, stepViewed, stepWorking].forEach(el => {
            el.className = "flex-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 rounded-xl p-4 flex flex-col items-center justify-center text-center space-y-1 shadow-md";
        });
        stepResolved.className = "flex-1 bg-emerald-500/20 text-emerald-400 border-2 border-emerald-400 rounded-xl p-4 flex flex-col items-center justify-center text-center space-y-1 shadow-xl scale-105 font-black";
        return;
    }

}

async function get_Categories_reports() {
    const ctxPie = document.getElementById('categoriesPieChart');
    const ctxBar = document.getElementById('monthlyBarChart');
    const response = await fetch("/dashboard",{
        method: "POST",
    })
    const data = await response.json();
    console.log(data["category_response"]);
    
    new Chart(ctxPie, {
        type: 'pie',
        data: {
            labels: data["category_response"]["labels"],
            datasets: [{
                data: data["category_response"]["values"],
                backgroundColor: ['#38bdf8', '#f43f5e', '#fb923c', '#facc15'],
                borderWidth: 2,
                borderColor: '#1e293b'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: '#94a3b8', font: { weight: 'bold' } }, position: 'top' }
            }
        }
    });  
    new Chart(ctxBar, {
        type: 'bar',
        data: {
            labels: data["month_response"]["labels"],
            datasets: [{
                label: 'Logged Complaints',
                data: data["month_response"]["values"],
                backgroundColor: '#0284c7',
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { ticks: { color: '#94a3b8' }, grid: { display: false } },
                y: { ticks: { color: '#94a3b8' }, grid: { color: '#334155/30' } }
            },
            plugins: { legend: { display: false } }
        }
    }); 
}

get_Categories_reports()