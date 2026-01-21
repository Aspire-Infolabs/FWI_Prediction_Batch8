const ctx2=document.getElementById("chart");
new Chart(ctx2,{
type:"bar",
data:{labels:["Temp","RH","Wind","Rain"],
datasets:[{data:[30,50,20,5],backgroundColor:"#ff9800"}]},
options:{plugins:{legend:{display:false}}}
});
