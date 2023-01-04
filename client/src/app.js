var express = require('express'); 
const {deleteProduct, insertProduct, listProducts, findById} = require('../grpc_client')

const app = express(); 

app.use(express.json()); 

app.get('/list', async (req, res) => 
{
    const products = await listProducts(); 
    res.status(200).send(products);
})

app.get('/find/:id', async (req, res) => 
{
    const product = await findById(req.params.id)
    res.status(200).send(product)
})

app.delete('/delete/:id', async (req, res) => 
{
    const product = await deleteProduct(req.params.id)
    res.status(200).send(product)
})

app.post('/insert', async (req, res) => 
{
    if(!req.body || req.body.name.trim() == "" ||  req.body.price == 0 || typeof req.body.price != Number) {
        res.status(400).send({msg: 'field is required'})
    }

    const {price, name} = req.body
    const prod = await insertProduct({price, name})
    res.status(200).send(prod)
})

const start = () => 
{
    app.listen(5050, () => console.log('Running'))
}

start(); 