#!/usr/bin/env python
# encoding: utf-8
"""
contacts.py

Created by Jeremiah Shirk on 2012-08-28.
Copyright (c) 2012 Monitis. All rights reserved.
"""

from monitis.api import get, post, MonitisError, validate_kwargs


def add_contact(**kwargs):
    ''' Add a new contact

    Required fields: firstName, lastName, account, contactType, timezone.

    Optional fields: group, sendDailyReport, sendWeeklyReport,
    sendMonthlyReport, portable, country, textType

    '''
    required = ['firstName', 'lastName', 'account', 'contactType', 'timezone']
    optional = ['sendDailyReport', 'sendWeeklyReport','sendMonthlyReport',
                'portable', 'country', 'textType']

    post_args = validate_kwargs(required, optional, **kwargs)
    return post(action='addContact', **post_args)


def edit_contact(**kwargs):
    '''  '''
    required = ['contactId']
    optional = ['firstName', 'lastName', 'account', 'contactType', 'timezone',
                'portable', 'code', 'country', 'textType']

    post_args = validate_kwargs(required, optional, **kwargs)
    return post(action='editContact', **post_args)


def delete_contact(contact_id=None, contact_type=None, account=None):
    ''' Delete a contact

    Required fields: contactId, or contactType AND account
    '''
    if not (contact_id or (contact_type and account)):
        raise MonitisError('Contact ID or Contact Type and Account required')

    if contact_id:
        return post(action='deleteContact', contactId=contact_id)
    else:
        return post(action='deleteContact', contactType=contact_type,
                    account=account)


def confirm_contact(**kwargs):
    ''' Confirm the specified contact '''
    required = ['contactId', 'confirmationKey']
    optional = []

    post_args = validate_kwargs(required, optional, **kwargs)
    return post(action='confirmContact', **post_args)


def contact_activate(**kwargs):
    ''' Activate the specified contact '''
    required = ['contactId']
    optional = []
    post_args = validate_kwargs(required, optional, **kwargs)
    return post(action='contactActivate', **post_args)


def contact_deactivate(**kwargs):
    ''' Deactivate the specified contact '''
    required = ['contactId']
    optional = []
    post_args = validate_kwargs(required, optional, **kwargs)
    return post(action='contactDeactivate', **post_args)


def get_contacts():
    ''' Get user's contacts '''
    return get(action='contactsList')


def get_contact_groups():
    ''' Get all contact groups for the user '''
    return get(action='contactGroupList')


def get_recent_alerts(**kwargs):
    ''' Get recent alerts history

    Start date and end date are in miliseconds since the Epoch'''
    required = []
    optional = ['timezone', 'startDate', 'endDate']
    post_args = validate_kwargs(required, optional, **kwargs)
    return get(action='recentAlerts', **post_args)
