class Reports:
    def __init__(self,cursor):
        self.cursor = cursor


    def get_categories_data(self):
        category_labels = []
        category_values = []
        self.cursor.execute("""
        Select ca.category_name,count(*) from complaints c join categories ca using(category_id) group by category_id;
        """)
        datas = self.cursor.fetchall()
        for data in datas:
            category_labels.append(data[0])
            category_values.append(data[1])
        return {
            "labels": category_labels,
            "values": category_values
        }
    
    def get_monthly_analytics_activity(self):

        monthly_labels = []
        monthly_values = []
        self.cursor.execute("""
        Select monthname(c.created_at) as Months,count(c.complaint_id) complains from complaints c where year(c.created_at) = (
        SELECT YEAR(CURDATE()) AS CurrentYear) group by Months;    
    """)
        datas = self.cursor.fetchall()
        for data in datas:
            monthly_labels.append(data[0])
            monthly_values.append(data[1])
        return {
            "labels": monthly_labels,
            "values": monthly_values
        }
    

    