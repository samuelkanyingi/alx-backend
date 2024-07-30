import redis from 'redis';

const client = redis.createClient();

client.on('connect', (err) => {
	console.log('Redis client connected to the server');
	});
client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

function createHash() {
	client.hset('HolbertonSchools', 'Portland', 50, redis.print);
	client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
	client.hset('HolbertonSchools', 'NewYork', 20, redis.print);
	client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
	client.hset('HolbertonSchools', 'Cali', 40, redis.print);
	client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}
function displayHash() {
	client.hgetall('HolbertonSchools', (err, reply) => {
	if (err) {
	console.error(`Error: ${err}`);
	} else {
		console.log(reply);
	}
	});
}
createHash();
displayHash();
