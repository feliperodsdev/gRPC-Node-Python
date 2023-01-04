var express = require('express'); 
const {deleteProduct, insertProduct, listProducts} = require('../grpc_client')

const app = express(); 

app.use(express.json()); 

app.get('/list', async (req, res) => 
{
    const products = await listProducts(); 
    res.status(200).send(products);
})

const start = () => 
{
    app.listen(5050, () => console.log('Running'))
}

start(); 