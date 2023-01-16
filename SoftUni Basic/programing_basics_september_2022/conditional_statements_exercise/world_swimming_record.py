record = float(input())
distance = float(input())
timing_per_meter = float(input())
total_seconds = (distance * timing_per_meter)
opposition = (distance//15) * 12.5
full_timing = total_seconds + opposition
if record < full_timing:
    delta = full_timing - record
    print(f"No, he failed! He was {delta:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {full_timing:.2f} seconds.")
    