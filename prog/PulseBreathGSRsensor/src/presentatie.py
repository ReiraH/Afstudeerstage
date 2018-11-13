
    while ser_bytes:
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("ascii"))
        
        t = decoded_bytes.split('  ')[0]
        p = decoded_bytes.split('  ')[1]
        b = decoded_bytes.split('  ')[2]
        g = decoded_bytes.split('  ')[3]
        
        current_time = datetime.datetime.now()
        datetime_now = current_time.strftime('%Y-%m-%d_%H:%M:%S.%f')

        t_ = t.split(': ')[1]
        p_ = p.split(': ')[1]
        b_ = b.split(': ')[1]
        g_ = g.split(': ')[1]

        data = [t, p, b, g, datetime_now]
        data_ = [t_, p_, b_, g_, datetime_now]
        
        convert_to_CSV(data_)
        data_list.append(data)
        ser_bytes = ser.readline()