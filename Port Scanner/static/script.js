function startScan(){
    const ip=document.getElementById('ip').value;
    if(!ip){
        alert('Please enter an IP Address!');
        return;
    }

    document.getElementById('loader').style.display='block';
    document.getElementById('resultTable').style.display='none';
    document.getElementById('results').innerHTML='';

    fetch('/scan',{
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ip: ip})
    })

    .then(response => response.json())
    .then(data => {
        document.getElementById('loader').style.display='none';
        const table= document.getElementById('resultTable');
        const results=document.getElementById('results');
        data.open_ports.forEach(port => {
            const row =document.createElement('tr');
            row.innerHTML=`<td class="open">${port}</td>`;
            results.appendChild(row);
        });
        table.style.display='table';
    })
    .catch(error => {
        document.getElementById('loader').style.display="none";
        alert('Error Scanning:' + error);
    })
}