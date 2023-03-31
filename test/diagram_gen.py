from diagrams import Diagram, Edge
from diagrams.generic.blank import Blank

with Diagram("Use Case Diagram", show=False, direction="TB"):
    tax_filer = Blank("Tax Filer")
    paralegal = Blank("Paralegal")
    chatbot = Blank("Chatbot")

    language_assistance = Blank("Language Assistance\n(Translate languages for tax filers)")
    tax_query_support = Blank("Tax Query Support\n(Answer tax-related queries)")
    conversational_continuity = Blank("Conversational Continuity\n(Save and resume chat conversations)")
    privacy_control = Blank("Privacy Control\n(Tax filers can prevent data saving)")
    paralegal_access = Blank("Paralegal Access\n(Access tax filer's financial summary)")
    case_referral = Blank("Case Referral\n(Send cases to appropriate departments)")

    tax_filer >> language_assistance >> chatbot
    tax_filer >> tax_query_support >> chatbot
    tax_filer >> conversational_continuity >> chatbot
    tax_filer >> privacy_control >> chatbot

    paralegal >> paralegal_access >> chatbot
    paralegal >> case_referral >> chatbot

