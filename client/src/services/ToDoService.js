// https://stackoverflow.com/questions/41164672/whats-the-equivalent-of-angular-service-in-vuejs/54165192#54165192

import axios from 'axios';

let baseUrl = "http://localhost:5000";
let axiosInstance = null;

export default new class {
    
    constructor(){
        axiosInstance = axios.create({
            baseURL: baseUrl,            
            headers: { 'Content-Type': 'application/json' }  
        });
    }

    getPong(){
        return axiosInstance("/ping");
    }

    getToDoList(){
        return axiosInstance("/todolist");
    }

    saveItem(item){
        return axiosInstance.post("/todolist", item);
    }

 }