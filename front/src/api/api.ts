import { AirConditionerSetting, Thermometer } from "@/type";
import axios from "axios";
import { Static } from "vue";
import { UpdateAirConditionerSetting } from '../type';

export class HomeServerApi {
    static HOST_URL = "http://mizserver:8000"
    static async getThermometer(): Promise<Thermometer[]> {
        return await axios.get(`${this.HOST_URL}/thermometer`).then((res) => {
            return res.data;
        });
    }
    static async getActiveAirConditionerSetting(): Promise<AirConditionerSetting> {
        return await axios.get(`${this.HOST_URL}/airConditionerSetting/active`).then((res) => {
            return res.data;
        });
    }
    static async updateAirConditionerSetting(mode: string, data: UpdateAirConditionerSetting) {
        return await axios.patch(`${this.HOST_URL}/airConditionerSetting/${mode}`, data).then((res) => {
            return res.data;
        });
    }
    static async updateAirConditionerToNonActive() {
        return await axios.post(`${this.HOST_URL}/airConditionerSetting/non-active`).then((res) => {
            return res.data;
        });
    }
}