emvTags = {
    '42': 'Issuer Identification Number (IIN)',
    '4F': 'Application Identifier (AID)',
    '50': 'Application Label',
    '57': 'Track 2 Equivalent Data',
    '5A': 'Application Primary Account Number (PAN)',
    '61': 'Application Template',
    '6F': 'File Control Information (FCI) Template',
    '70': 'EMV Proprietary Template',
    '71': 'Issuer Script Template 1',
    '72': 'Issuer Script Template 2',
    '73': 'Directory Discretionary Template',
    '77': 'Response Message Template Format 2',
    '80': 'Response Message Template Format 1',
    '81': 'Amount, Authorised (Binary)',
    '82': 'Application Interchange Profile',
    '83': 'Command Template',
    '84': 'Dedicated File (DF) Name',
    '86': 'Issuer Script Command',
    '87': 'Application Priority Indicator',
    '88': 'Short File Identifier (SFI)',
    '89': 'Authorisation Code',
    '8A': 'Authorisation Response Code',
    '8C': 'Card Risk Management Data Object List 1 (CDOL1)',
    '8D': 'Card Risk Management Data Object List 2 (CDOL2)',
    '8E': 'Cardholder Verification Method (CVM) List',
    '8F': 'Certification Authority Public Key Index',
    '90': 'Issuer Public Key Certificate',
    '91': 'Issuer Authentication Data',
    '92': 'Issuer Public Key Remainder',
    '93': 'Signed Static Application Data',
    '94': 'Application File Locator (AFL)',
    '95': 'TerminalClasses Verification Results',
    '97': 'Transaction Certificate Data Object List (TDOL)',
    '98': 'Transaction Certificate (TC) Hash Value',
    '99': 'Transaction Personal Identification Number (PIN) Data',
    '9A': 'Transaction Date',
    '9B': 'Transaction Status Information',
    '9C': 'Transaction Type',
    '9D': 'Directory Definition File (DDF) Name',
    'A5': 'File Control Information (FCI) Proprietary Template',
    '5F20': 'Cardholder Name',
    '5F24': 'Application Expiration Date',
    '5F25': 'Application Effective Date',
    '5F28': 'Issuer Country Code',
    '5F2A': 'Transaction Currency Code',
    '5F2D': 'Language Preference',
    '5F30': 'Service Code',
    '5F34': 'Application Primary Account Number (PAN)',
    '5F36': 'Transaction Currency Exponent',
    '5F50': 'Issuer URL',
    '5F53': 'International Bank Account Number (IBAN)',
    '5F54': 'Bank Identifier Code (BIC)',
    '5F55': 'Issuer Country Code (alpha2 format)',
    '5F56': 'Issuer Country Code (alpha3 format)',
    '9F01': 'Acquirer Identifier',
    '9F02': 'Amount, Authorised (Numeric)',
    '9F03': 'Amount, Other (Numeric)',
    '9F04': 'Amount, Other (Binary)',
    '9F05': 'Application Discretionary Data',
    '9F06': 'Application Identifier (AID) - terminal',
    '9F07': 'Application Usage Control',
    '9F08': 'Application Version Number',
    '9F09': 'Application Version Number',
    '9F0B': 'Cardholder Name Extended',
    '9F0D': 'Issuer Action Code - Default',
    '9F0E': 'Issuer Action Code - Denial',
    '9F0F': 'Issuer Action Code - Online',
    '9F10': 'Issuer Application Data',
    '9F11': 'Issuer Code Table Index',
    '9F12': 'Application Preferred Name',
    '9F13': 'Last Online Application Transaction Counter (ATC) Register',
    '9F14': 'Lower Consecutive Offline Limit',
    '9F15': 'Merchant Category Code',
    '9F16': 'Merchant Identifier',
    '9F17': 'Personal Identification Number (PIN) Try Counter',
    '9F18': 'Issuer Script Identifier',
    '9F1A': 'TerminalClasses Country Code',
    '9F1B': 'TerminalClasses Floor Limit',
    '9F1C': 'TerminalClasses Identification',
    '9F1D': 'TerminalClasses Risk Management Data',
    '9F1E': 'Interface Device (IFD) Serial Number',
    '9F1F': 'Track 1 Discretionary Data',
    '9F20': 'Track 2 Discretionary Data',
    '9F21': 'Transaction Time',
    '9F22': 'Certification Authority Public Key Index',
    '9F23': 'Upper Consecutive Offline Limit',
    '9F26': 'Application Cryptogram',
    '9F27': 'Cryptogram Information Data',
    '9F2D': ('Integrated Circuit Card (ICC) PIN '
             'Encipherment Public Key Certificate'),
    '9F2E': ('Integrated Circuit Card (ICC) PIN '
             'Encipherment Public Key Exponent'),
    '9F2F': ('Integrated Circuit Card (ICC) PIN '
             'Encipherment Public Key Remainder'),
    '9F32': 'Issuer Public Key Exponent',
    '9F33': 'TerminalClasses Capabilities',
    '9F34': 'Cardholder Verification Method (CVM) Results',
    '9F35': 'TerminalClasses Type',
    '9F36': 'Application Transaction Counter (ATC)',
    '9F37': 'Unpredictable Number',
    '9F38': 'Processing Options Data Object List (PDOL)',
    '9F39': 'Point-of-Service (POS) Entry Mode',
    '9F3A': 'Amount, Reference Currency',
    '9F3B': 'Application Reference Currency',
    '9F3C': 'Transaction Reference Currency Code',
    '9F3D': 'Transaction Reference Currency Exponent',
    '9F40': 'Additional TerminalClasses Capabilities',
    '9F41': 'Transaction Sequence Counter',
    '9F42': 'Application Currency Code',
    '9F43': 'Application Reference Currency Exponent',
    '9F44': 'Application Currency Exponent',
    '9F45': 'Data Authentication Code',
    '9F46': 'Integrated Circuit Card (ICC) Public Key Certificate',
    '9F47': 'Integrated Circuit Card (ICC) Public Key Exponent',
    '9F48': 'Integrated Circuit Card (ICC) Public Key Remainder',
    '9F49': 'Dynamic Data Authentication Data Object List (DDOL)',
    '9F4A': 'Static Data Authentication Tag List',
    '9F4B': 'Signed Dynamic Application Data',
    '9F4C': 'ICC Dynamic Number',
    '9F4D': 'Log Entry',
    '9F4E': 'Merchant Name and Location',
    '9F4F': 'Log Format',
    '9F51': 'Application Currency Code',
    '9F52': 'Card Verification Results (CVR)',
    '9F53': 'Consecutive Transaction Limit (International)',
    '9F54': 'Cumulative Total Transaction Amount Limit',
    '9F55': 'Geographic Indicator',
    '9F56': 'Issuer Authentication Indicator',
    '9F57': 'Issuer Country Code',
    '9F58': 'Lower Consecutive Offline Limit (Card Check)',
    '9F59': 'Upper Consecutive Offline Limit (Card Check)',
    '9F5A': 'Issuer URL2',
    '9F5C': 'Cumulative Total Transaction Amount Upper Limit',
    '9F65': 'Track 2 Bit Map for CVC3',
    '9F66': 'Track 2 Bit Map for UN and ATC',
    '9F68': 'Mag Stripe CVM List',
    '9F69': 'Unpredictable Number Data Object List (UDOL)',
    '9F6B': 'Track 2 Data',
    '9F6C': 'Mag Stripe Application Version Number (Card)',
    '9F6E': 'Unknown Tag',
    '9F72': 'Consecutive Transaction Limit (International - Country)',
    '9F73': 'Currency Conversion Factor',
    '9F74': 'VLP Issuer Authorization Code',
    '9F75': 'Cumulative Total Transaction Amount Limit - Dual Currency',
    '9F76': 'Secondary Application Currency Code',
    '9F7F': 'Card Production Life Cycle (CPLC) History File Identifiers',
    'BF0C': 'FCI Issuer Discretionary Data',
    'DF01': 'Reference PIN',
    }


def get_tag_meaning(tag):
    try:
        return emvTags[tag]
    except KeyError:
        return f'Meaning Unknown for tag "{tag}"'
