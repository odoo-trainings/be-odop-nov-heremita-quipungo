
{
    "name": "Kawiil Financing",
    "summary": "Streamlines the loan application process for dealerships.",
    "category": "Kawiil/Custom Modules",
    "version": "1.0.0",
    "author": "ODOP Trainee",
    "maintainer": "José M. Quipungo",  #
    "website": "https://tis.ao",
    "depends": ["base"],
    "license": "OPL-1",
    # XML and CSV files Odoo loads on install, in the order you list them.
    #
    # Register each file in the assignment that creates it, and only then.
    # Listing a file before its models exist crashes the install, so add the
    # lines marked 2.06 when you get to 2.06, not now.
    #
    # Order is not cosmetic. Odoo resolves external ids as it reads, so a file
    # can only refer to something a file above it already created: security,
    # then data, then views, then the menu that points at them. The list grows
    # by insertion, not by appending: at 2.07 the security files go in above
    # the views you added at 2.06.
    #
    # The finished list, with the assignment that adds each line:
    #     "security/kawiil_financing_groups.xml",             2.07
    #     "security/ir.access.csv",                           2.07
    #     "data/ir_sequence_data.xml",                        3.07
    #     "views/loan_application_views.xml",                 2.06
    #     "views/loan_application_tag_views.xml",             2.09
    #     "views/loan_application_document_type_views.xml",   2.09
    #     "views/res_partner_views.xml",                      4.01
    #     "views/kawiil_financing_menu.xml",                  2.06
    #
    # Assignment 2.09: the three new models need access rows too. A CSV file
    # cannot hold comments, so they wait here instead. Copy these lines to the
    # end of security/ir.access.csv when you reach 2.09, not before: a row
    # for a model that does not exist yet stops the install.
    #
    #     access_loan_application_tag_user,loan.application.tag.user,True,model_loan_application_tag,group_kawiil_financing_user,r,,"Users pick tags on a loan, only admins manage the list."
    #     access_loan_application_tag_admin,loan.application.tag.admin,True,model_loan_application_tag,group_kawiil_financing_admin,crud,,"Admins manage the tag list."
    #     access_loan_application_document_type_user,loan.application.document.type.user,True,model_loan_application_document_type,group_kawiil_financing_user,r,,"Users see which documents a loan needs, only admins decide that."
    #     access_loan_application_document_type_admin,loan.application.document.type.admin,True,model_loan_application_document_type,group_kawiil_financing_admin,crud,,"Admins decide which documents a loan needs."
    #     access_loan_application_document_user,loan.application.document.user,True,model_loan_application_document,group_kawiil_financing_user,crud,,"Users fill in the compliance checklist of their loans."
    #     access_loan_application_document_admin,loan.application.document.admin,True,model_loan_application_document,group_kawiil_financing_admin,crud,,"Admins have full access to every checklist."
    "data": [],
    # Sample records, loaded only when a database is created with demo data.
    #
    # Same rule as above, one line per assignment, inserted in order.
    # Configuration data before transactional data, so the loans can refer to
    # tags that already exist:
    #     "demo/config_demo.xml",   2.09
    #     "demo/loan_demo.xml",     2.04
    "demo": [],
    # True gives the module its own top-level menu and makes it show up as an
    # app. False would make it a technical module that only extends others.
    "application": True,
}
