public enum ParkingStatus {
    EMPTY,
    OCCUPIED;
}

public class ParkingSlot {
    private String slotId;
    private String slotNumber;
    private ParkingStatus status;
    private SlotSize slotSize;
    private Vehicle vehicle;

    public ParkingSLot(String slotId, 
                       String slotNumber,
                       ParkingStatus status,
                       SlotSize slotSize
                       ) {
        this.slotId = slotId;
        this.slotNumber = slotNumber;
        this.status = status;
        this.slotSize = slotSize;
    }

    public void parkVehicle(Vehicle vehicle) {
        if (this.slotSize.isVehicleParkingPossible(vehicle)) {
            this.vehicle = vehicle;
            status = ParkingStatus.OCCUPIED;
        } else {
            throw new IllegalArgumentException("parking not possible for this vehicle type");
        }
    }

    public void emptySlot(){
        this.vehicle = null;
        status = ParkingStatus.EMPTY;
    }
}

public class Floor {
    private String floorId;
    private int floorNumber;
    private String floorName;
    private List<ParkingSlot> parkingSlots;

    public Floor(String floorId, int floorNumber, String floorName, List<ParkingSlot> parkingSlots) {
        this.floorId = floorId;
        this.floorName = floorName;
        this.floorNumber = floorNumber;
        this.parkingSlots = parkingSlots;
    }

    public void emptyFloor(){
        for (ParkingSlot slot: parkingSlots) {
            slot.emptySlot();
        }
    }
}

