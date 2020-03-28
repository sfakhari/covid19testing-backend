from flask import Blueprint, jsonify, make_response, request, abort, current_app as app
from .models import Entities, db
import json
from datetime import datetime
from flask_basicauth import BasicAuth

# Create blueprint
database_bp = Blueprint('database', __name__)

basic_auth = BasicAuth(app)

@database_bp.route('/api/v1/location', methods=['GET'])
def list_location():
  """
  list all locations
  """
  table_data = Entities.query.order_by(Entities.record_id).all()
  data_list = []
  for data in table_data:
    data_list.append(
      {
        'additional_information_for_patients': data.additional_information_for_patients,
        'created_on': data.created_on,
        'data_source': data.data_source,
        'deleted_on': data.deleted_on,
        'geojson': data.geojson,
        'is_collecting_samples': data.is_collecting_samples,
        'is_collecting_samples_by_appointment_only': data.is_collecting_samples_by_appointment_only,
        'is_collecting_samples_for_others': data.is_collecting_samples_for_others,
        'is_collecting_samples_onsite': data.is_collecting_samples_onsite,
        'is_evaluating_symptoms': data.is_evaluating_symptoms,
        'is_evaluating_symptoms_by_appointment_only': data.is_evaluating_symptoms_by_appointment_only,
        'is_hidden': data.is_hidden,
        'is_ordering_tests': data.is_ordering_tests,
        'is_ordering_tests_only_for_those_who_meeting_criteria': data.is_ordering_tests_only_for_those_who_meeting_criteria,
        'is_processing_samples': data.is_processing_samples ,
        'is_processing_samples_for_others': data.is_processing_samples_for_others,
        'is_processing_samples_onsite': data.is_processing_samples_onsite,
        'is_verified': data.is_verified,
        'location_address_locality': data.location_address_locality,
        'location_address_postal_code': data.location_address_postal_code,
        'location_address_region': data.location_address_region,
        'location_address_street': data.location_address_street,
        'location_contact_phone_appointments': data.location_contact_phone_appointments,
        'location_contact_phone_covid': data.location_contact_phone_covid,
        'location_contact_phone_main': data.location_contact_phone_main,
        'location_contact_url_covid_appointments': data.location_contact_url_covid_appointments,
        'location_contact_url_covid_info': data.location_contact_url_covid_info,
        'location_contact_url_covid_screening_tool': data.location_contact_url_covid_screening_tool,
        'location_contact_url_covid_virtual_visit': data.location_contact_url_covid_virtual_visit,
        'location_contact_url_main': data.location_contact_url_main,
        'location_hours_of_operation': data.location_hours_of_operation,
        'location_id': data.location_id,
        'location_latitude': data.location_latitude,
        'location_longitude': data.location_longitude,
        'location_name': data.location_name,
        'location_place_of_service_type': data.location_place_of_service_type,
        'location_specific_testing_criteria': data.location_specific_testing_criteria,
        'raw_data': data.raw_data,
        'reference_publisher_of_criteria': data.reference_publisher_of_criteria,
        'updated_on': data.updated_on,
        'record_id': data.record_id
      }
    )
  

  return jsonify(data_list)

@database_bp.route('/api/v1/location', methods=['POST'])
@basic_auth.required
def create_location():
  """
  create new location
  """

  # Error if json is not present
  if not request.json:
    abort(400)
  
  # Get data from json 
  content = request.get_json()

  # Map json data to Entities model
  if isinstance(content, list):
    for data in content:
      data = Entities(
        additional_information_for_patients=data.get("additional_information_for_patients"),
        created_on=data.get("created_on"),
        data_source=data.get("data_source"),
        deleted_on=data.get("deleted_on"),
        geojson=data.get("geojson"),
        is_collecting_samples=bool(data.get("is_collecting_samples")),
        is_collecting_samples_by_appointment_only=bool(data.get("is_collecting_samples_by_appointment_only")),
        is_collecting_samples_for_others=bool(data.get("is_collecting_samples_for_others")),
        is_collecting_samples_onsite=bool(data.get("is_collecting_samples_onsite")),
        is_evaluating_symptoms=bool(data.get("is_evaluating_symptoms")),
        is_evaluating_symptoms_by_appointment_only=bool(data.get("is_evaluating_symptoms_by_appointment_only")),
        is_hidden=bool(data.get("is_hidden")),
        is_ordering_tests=bool(data.get("is_ordering_tests")),
        is_ordering_tests_only_for_those_who_meeting_criteria=bool(data.get("is_ordering_tests_only_for_those_who_meeting_criteria")),
        is_processing_samples=bool(data.get("is_processing_samples")),
        is_processing_samples_for_others=bool(data.get("is_processing_samples_for_others")),
        is_processing_samples_onsite=bool(data.get("is_processing_samples_onsite")),
        is_verified=bool(data.get("is_verified")),
        location_address_locality=data.get("location_address_locality"),
        location_address_postal_code=data.get("location_address_postal_code"),
        location_address_region=data.get("location_address_region"),
        location_address_street=data.get("location_address_street"),
        location_contact_phone_appointments=data.get("location_contact_phone_appointments"),
        location_contact_phone_covid=data.get("location_contact_phone_covid"),
        location_contact_phone_main=data.get("location_contact_phone_main"),
        location_contact_url_covid_appointments=data.get("location_contact_url_covid_appointments"),
        location_contact_url_covid_info=data.get("location_contact_url_covid_info"),
        location_contact_url_covid_screening_tool=data.get("location_contact_url_covid_screening_tool"),
        location_contact_url_covid_virtual_visit=data.get("location_contact_url_covid_virtual_visit"),
        location_contact_url_main=data.get("location_contact_url_main"),
        location_hours_of_operation=data.get("location_hours_of_operation"),
        location_id=data.get("location_id"),
        location_latitude=data.get("location_latitude"),
        location_longitude=data.get("location_longitude"),
        location_name=data.get("location_name"),
        location_place_of_service_type=data.get("location_place_of_service_type"),
        location_specific_testing_criteria=data.get("location_specific_testing_criteria"),
        raw_data=data.get("raw_data"),
        reference_publisher_of_criteria=data.get("reference_publisher_of_criteria"),
        updated_on=data.get("updated_on"),
        record_id=data.get("record_id")
      )
      # Commit to DB
      db.session.add(data)
      db.session.commit()

  else:
    data = Entities(
        additional_information_for_patients=content.get("additional_information_for_patients"),
        created_on=content.get("created_on"),
        data_source=content.get("data_source"),
        deleted_on=content.get("deleted_on"),
        geojson=content.get("geojson"),
        is_collecting_samples=bool(content.get("is_collecting_samples")),
        is_collecting_samples_by_appointment_only=bool(content.get("is_collecting_samples_by_appointment_only")),
        is_collecting_samples_for_others=bool(content.get("is_collecting_samples_for_others")),
        is_collecting_samples_onsite=bool(content.get("is_collecting_samples_onsite")),
        is_evaluating_symptoms=bool(content.get("is_evaluating_symptoms")),
        is_evaluating_symptoms_by_appointment_only=bool(content.get("is_evaluating_symptoms_by_appointment_only")),
        is_hidden=bool(content.get("is_hidden")),
        is_ordering_tests=bool(content.get("is_ordering_tests")),
        is_ordering_tests_only_for_those_who_meeting_criteria=bool(content.get("is_ordering_tests_only_for_those_who_meeting_criteria")),
        is_processing_samples=bool(content.get("is_processing_samples")),
        is_processing_samples_for_others=bool(content.get("is_processing_samples_for_others")),
        is_processing_samples_onsite=bool(content.get("is_processing_samples_onsite")),
        is_verified=bool(content.get("is_verified")),
        location_address_locality=content.get("location_address_locality"),
        location_address_postal_code=content.get("location_address_postal_code"),
        location_address_region=content.get("location_address_region"),
        location_address_street=content.get("location_address_street"),
        location_contact_phone_appointments=content.get("location_contact_phone_appointments"),
        location_contact_phone_covid=content.get("location_contact_phone_covid"),
        location_contact_phone_main=content.get("location_contact_phone_main"),
        location_contact_url_covid_appointments=content.get("location_contact_url_covid_appointments"),
        location_contact_url_covid_info=content.get("location_contact_url_covid_info"),
        location_contact_url_covid_screening_tool=content.get("location_contact_url_covid_screening_tool"),
        location_contact_url_covid_virtual_visit=content.get("location_contact_url_covid_virtual_visit"),
        location_contact_url_main=content.get("location_contact_url_main"),
        location_hours_of_operation=content.get("location_hours_of_operation"),
        location_id=content.get("location_id"),
        location_latitude=content.get("location_latitude"),
        location_longitude=content.get("location_longitude"),
        location_name=content.get("location_name"),
        location_place_of_service_type=content.get("location_place_of_service_type"),
        location_specific_testing_criteria=content.get("location_specific_testing_criteria"),
        raw_data=content.get("raw_data"),
        reference_publisher_of_criteria=content.get("reference_publisher_of_criteria"),
        updated_on=content.get("updated_on"),
        record_id=content.get("record_id")
      )
    # Commit to DB
    db.session.add(data)
    db.session.commit()

  return jsonify(result="accepted"), 201
  

@database_bp.route('/api/v1/location/<location_id>', methods=['GET'])
def get_location(location_id):
  data = Entities.query.filter(Entities.location_id == location_id).first()
  result = {
        'additional_information_for_patients': data.additional_information_for_patients,
        'created_on': data.created_on,
        'data_source': data.data_source,
        'deleted_on': data.deleted_on,
        'geojson': data.geojson,
        'is_collecting_samples': data.is_collecting_samples,
        'is_collecting_samples_by_appointment_only': data.is_collecting_samples_by_appointment_only,
        'is_collecting_samples_for_others': data.is_collecting_samples_for_others,
        'is_collecting_samples_onsite': data.is_collecting_samples_onsite,
        'is_evaluating_symptoms': data.is_evaluating_symptoms,
        'is_evaluating_symptoms_by_appointment_only': data.is_evaluating_symptoms_by_appointment_only,
        'is_hidden': data.is_hidden,
        'is_ordering_tests': data.is_ordering_tests,
        'is_ordering_tests_only_for_those_who_meeting_criteria': data.is_ordering_tests_only_for_those_who_meeting_criteria,
        'is_processing_samples': data.is_processing_samples ,
        'is_processing_samples_for_others': data.is_processing_samples_for_others,
        'is_processing_samples_onsite': data.is_processing_samples_onsite,
        'is_verified': data.is_verified,
        'location_address_locality': data.location_address_locality,
        'location_address_postal_code': data.location_address_postal_code,
        'location_address_region': data.location_address_region,
        'location_address_street': data.location_address_street,
        'location_contact_phone_appointments': data.location_contact_phone_appointments,
        'location_contact_phone_covid': data.location_contact_phone_covid,
        'location_contact_phone_main': data.location_contact_phone_main,
        'location_contact_url_covid_appointments': data.location_contact_url_covid_appointments,
        'location_contact_url_covid_info': data.location_contact_url_covid_info,
        'location_contact_url_covid_screening_tool': data.location_contact_url_covid_screening_tool,
        'location_contact_url_covid_virtual_visit': data.location_contact_url_covid_virtual_visit,
        'location_contact_url_main': data.location_contact_url_main,
        'location_hours_of_operation': data.location_hours_of_operation,
        'location_id': data.location_id,
        'location_latitude': data.location_latitude,
        'location_longitude': data.location_longitude,
        'location_name': data.location_name,
        'location_place_of_service_type': data.location_place_of_service_type,
        'location_specific_testing_criteria': data.location_specific_testing_criteria,
        'raw_data': data.raw_data,
        'reference_publisher_of_criteria': data.reference_publisher_of_criteria,
        'updated_on': data.updated_on,
        'record_id': data.record_id
      }
  

  return jsonify(result)

@database_bp.route('/api/v1/location/<id>', methods=['POST'])
@basic_auth.required
def update_location(id):
  return jsonify("Not Implemented"), 501
