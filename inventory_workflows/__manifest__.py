{
    'name':   'Inventory Workflows',
    'author': 'Hafeez Brothers',
    'license': 'LGPL-3',
    'version' : '1.0',
    'depends': [
                'base',
                
                'stock'
                
                ],
    
    'data': [
      
        'Views/stock_picking_workflow.xml',
        'security/hr_user_rights_inventory.xml'
    ],
    
    'application': True,
    'price':25.00,
    'currency':'EUR', 
}
