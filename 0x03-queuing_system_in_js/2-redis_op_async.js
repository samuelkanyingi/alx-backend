import redis from 'redis';
import { promisify } from 'util';
const client  =  redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`)
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value,(err, reply) => { 
	if (err) {
	console.error(`Error setting school:${err}`);
	} else {
		console.log(`${reply}`);
	}
	})
}
async function displaySchoolValue(schoolName) {
	try { 
		const reply = await getAsync(schoolName);
		console.log(reply);
	} catch (err) {
		console.error(`Error: ${err}`);
	}
}
async function main() {
	await displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	await displaySchoolValue('HolbertonSanFrancisco');
}
main();
