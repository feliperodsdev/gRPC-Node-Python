var PROTO_PATH = __dirname + "/product.proto";
var grpc = require("@grpc/grpc-js");
var protoLoader = require("@grpc/proto-loader");

var packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

var protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
const client = new protoDescriptor.ProductService(
  "0.0.0.0:50051",
  grpc.credentials.createInsecure()
);

const findById = async (id) => {
  const prod = await new Promise((resolve, reject) => {
    client.Find({ id: id }, function (err, response) {
      if (err) reject(err);
      resolve(response);
    });
  });
  return prod;
};

const insertProduct = async (prod) => {
  const prodToAdd = await new Promise((resolve, reject) => {
    client.Insert(prod, function (err, response) {
      if (err) reject(err);
      resolve(response);
    });
  });
  return prodToAdd;
};

const listProducts = async () => {
  const prods = await new Promise((resolve, reject) => {
    client.List({}, function (err, response) {
      if (err) reject(err);
      resolve(response);
    });
  });
  return prods;
};

const deleteProduct = async (id) => {
  const prodToDelete = await new Promise((resolve, reject) => {
    client.Delete({ id: id }, function (err, response) {
      if (err) reject(err);
      resolve(response);
    });
  });
  return prodToDelete;
};

module.exports = {
  deleteProduct,
  listProducts,
  insertProduct,
  findById,
};
