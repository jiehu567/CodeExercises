class ParkingLots {
    
}

class Floor {

}


// 1. status check
// 2. parking

public enum ParkingLotStatus {
    EMPTY,
    OCCUPIED
}

public enum ParkAble {

}

class OneParkingLot {
    private ParkingLotStatus status;
    private VehicleType parkingLotType;

    public OneParkingLot (VehicleType parkingLotType){
        this.status = ParkingLotStatus.EMPTY;
        this.parkingLotType = parkingLotType;
    }

    public ParkingLotStatus getStatus(){
        return this.status;
    }

    public void parkVehicle (Vehicle vehicle){
        if (this.parkingLotType == vehicle.getType()) {
            this.status = ParkingLotStatus.OCCUPIED;
        } else {
            throw IllegalArgumentException("Not able to park in this slot");
        }
    }
}

public enum VehicleType {
    MOTOR,
    COMPACT,
    SEDAN,
    PEKKA
}

public interface Vehicle {
    public VehicleType getType();
}

public class MotorBike implements Vehicle {
    private VehicleType vehicleType;
    private String vehicleNumber;

    public MotorBike(String vehicleNumber) {
        this.vehicleType = VehicleType.MOTOR;
        this.vehicleNumber = vehicleNumber;
    }

    @Override
    public VehicleType getType() {
        return this.vehicleType;
    }

    @Override
    public String toString(){
        return "Vehicle: " + this.vehicleType.toString() + ", Number: " + this.vehicleNumber;
    }
}

public class CompactCar implements Vehicle {
    private VehicleType vehicleType;
    private String vehicleNumber;

    public CompactCar(String vehicleNumber) {
        this.vehicleType = VehicleType.COMPACT;
        this.vehicleNumber = vehicleNumber;
    }

    @Override
    public VehicleType getType() {
        return this.vehicleType;
    }

    @Override
    public String toString(){
        return "Vehicle: " + this.vehicleType.toString() + ", Number: " + this.vehicleNumber;
    }
}

