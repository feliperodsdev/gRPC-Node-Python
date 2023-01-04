var PROTO_PATH = __dirname + '/product.proto';
var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');

var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    });

var protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
const client = new protoDescriptor.ProductService('0.0.0.0:50051', grpc.credentials.createInsecure());


const insertProduct = (prod) => 
{
    client.Insert(prod, function(err, response){
        console.log(response)
    })
}

const listProducts = async () => 
{
    const prods = await new Promise((resolve, reject)=>{
        client.list({},function(err, response){
          if(err) reject (err)
          resolve(response)
        }
    )})
    return prods; 
}

const deleteProduct = (id) => 
{
    client.Delete({id: id}, function(err, response){
        console.log(response)
    })
}

module.exports = {
    deleteProduct, 
    listProducts, 
    insertProduct
}