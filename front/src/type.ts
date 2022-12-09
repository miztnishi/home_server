
export class Thermometer {
    id: number;
    date: Date;
    temperature: number;
    humidity: number;
    createdAt: Date;
    updatedAt: Date;
}

export class AirConditionerSetting {
    id: number;
    temperature: number;
    threshold: number
    mode: AirConditionerModeType
    isActive: boolean
}

export type AirConditionerModeType = "cooling" | "heating"

// エアコン閾値設定更新時
export class UpdateAirConditionerSetting {
    temperature: number
    threshold: number
}

