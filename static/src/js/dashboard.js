function show_time() {
    const live_timestamp = document.getElementById("live-timestamp");
    const date = new Date();
    live_timestamp.innerHTML= `<i class="fa-solid fa-circle text-emerald-400 animate-pulse text-[8px] mr-1.5"></i> Live Monitor: ${date.toLocaleDateString()} | ${date.toLocaleTimeString()}`
}
setInterval(() => {
    show_time()
}, 1000);

