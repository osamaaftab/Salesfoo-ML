from rest_framework import serializers


class LeadSerializer(serializers.Serializer):

    sex = serializers.CharField()
    days_since_signup = serializers.IntegerField()
    job_title = serializers.CharField()
    completed_form = serializers.IntegerField()
    visited_pricing = serializers.IntegerField()
    registered_for_webinar = serializers.IntegerField()
    attended_webinar = serializers.IntegerField()
    converted = serializers.IntegerField()
    is_manager = serializers.IntegerField()
    acquisition_channel_Cold_Call = serializers.IntegerField()
    acquisition_channel_Cold_Email = serializers.IntegerField()
    acquisition_channel_Organic_Search = serializers.IntegerField()
    acquisition_channel_Paid_Leads = serializers.IntegerField()
    acquisition_channel_Paid_Search = serializers.IntegerField()
    company_size_1_to_10 = serializers.IntegerField()
    company_size_11_to_50 = serializers.IntegerField()
    company_size_51_to_100 = serializers.IntegerField()
    company_size_101_to_250 = serializers.IntegerField()
    company_size_251_to_1000 = serializers.IntegerField()
    company_size_1000_to_10000 = serializers.IntegerField()
    company_size_10001_plus = serializers.IntegerField()
    industry_Financial_Services = serializers.IntegerField()
    industry_Furniture = serializers.IntegerField()
    industry_Heavy_Manufacturing = serializers.IntegerField()
    industry_Scandanavion_Design = serializers.IntegerField()
    industry_Transportation = serializers.IntegerField()
    industry_Web_Internet = serializers.IntegerField()
    email = serializers.EmailField()
    year = serializers.IntegerField()
    age = serializers.IntegerField()