const express = require('express');
const fs = require('fs');

const app = express();

app.get('/getnews', (req, res) => {
    const data = JSON.parse(fs.readFileSync('content.json'));
    const news=data.map(datax=>datax.haber_aciklama)
    const haberListesi = news.map(haber => `<li>${haber}</li>`).join(''); // her haber öğesi için bir li etiketi oluştur

  const html = `
    <html>
      <head>
        <title>Haberler</title>
      </head>
      <body>
        <ul>
          ${haberListesi}
        </ul>
      </body>
    </html>
  `;

  res.send(html);
  });
app.listen(3000,()=>{
console.log('port is ready')
})
