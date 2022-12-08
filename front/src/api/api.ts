import { Thermometer } from "@/type";
import axios from "axios";
import { Static } from "vue";

export class HomeServerApi {
    static HOST_URL = "http://mizserver:8000"
    static async getThermometer(): Promise<Thermometer[]> {
        return await axios.get(`${this.HOST_URL}/thermometer`).then((res) => {
            return res.data;
        });
    }
}