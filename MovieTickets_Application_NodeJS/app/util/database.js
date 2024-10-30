const { MongoClient } = require('mongodb');

let client;
let db;

async function getDatabase() {
    if (!client) {
        const uri = "mongodb+srv://workportal1992:gFYgIJRE5WZHc5yf@cluster0.a7j0f.mongodb.net/";
        client = new MongoClient(uri);

        try {
            // Connect the client
            await client.connect();
            console.log('Connected to MongoDB');
            
            // Get the database instance
            db = client.db('myDB');
        } catch (error) {
            console.error('MongoDB connection failed:', error);
            throw error;
        }
    }
    
    return db;
}

module.exports = { getDatabase };