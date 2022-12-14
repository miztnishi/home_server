import { AirConditionerSetting, Thermometer } from "@/type";
import axios from "axios";
import { UpdateAirConditionerSetting } from '../type';

export class HomeServerApi {
    static HOST_URL = "http://mizserver:8000"
    static async getThermometer(start: string, end: string): Promise<Thermometer[]> {
        return await axios.get(`${this.HOST_URL}/thermometer?start=${start}&end=${end}`).then((res) => {
            return res.data;
        });
    }
    static async getActiveAirConditionerSetting(): Promise<AirConditionerSetting[]> {
        return await axios.get(`${this.HOST_URL}/airConditionerSetting`).then((res) => {
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
    static async sendSignalAirConditioner() {
        return await axios.post(`${this.HOST_URL}/airConditioner/send-signal`).then((res) => {
            return res.data;
        });
    }
    static async sendSignalAirConditionerOff() {
        return await axios.post(`${this.HOST_URL}/airConditioner/send-signal/off`).then((res) => {
            return res.data;
        });
    }
    static async sendSignalLed(mode: string) {
        return await axios.post(`${this.HOST_URL}/LED/mode/${mode}`).then((res) => {
            return res.data;
        });
    }
}