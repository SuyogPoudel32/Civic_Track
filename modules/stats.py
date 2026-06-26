def get_reports(cursor):
    all_reports =[]
    cursor.execute("select count(*) from complaints")
    
    total_reports = cursor.fetchone()[0]
    all_reports.append({
        "Total Reports":total_reports
    })
    for status  in ["Under Review","In Progress","Resolved"]:
        cursor.execute(
            "SELECT COUNT(*) FROM complaints WHERE status = %s",
            (status,)
        )
        fetch_data = cursor.fetchone()[0]
        all_reports.append({
          status :fetch_data
        })
    return all_reports