import unittest
from modules.TI.threat_intelligence import ThreatIntelligence

class TestThreatIntelligence(unittest.TestCase):

    def test_arguments(self):
        # Valide arguments
        ti = ThreatIntelligence('download_script.sh', 'API_KEY', 'feed_folder')
        self.assertEqual(ti.download_file, 'download_script.sh')
        self.assertEqual(ti.abuse_api_key, 'API_KEY')
        self.assertEqual(ti.feed_folder, 'feed_folder')

        # Invalide(None) arguments
        with self.assertRaises(TypeError, msg="Arguments cannot be None or empty"):
            ti = ThreatIntelligence(None, 'API_KEY', 'feed_folder')
        with self.assertRaises(TypeError, msg="Expected TypeError for None argument"):
            ti = ThreatIntelligence('download_script.sh', None, 'feed_folder')
        with self.assertRaises(TypeError, msg="Expected TypeError for None argument"):
            ti = ThreatIntelligence('download_script.sh', 'API_KEY', None)

        # Invalide(blank) arguments
        with self.assertRaises(TypeError, msg="Expected TypeError for blank argument"):
            ti = ThreatIntelligence('', 'API_KEY', 'feed_folder')
        with self.assertRaises(TypeError, msg="Expected TypeError for blank argument"):
            ti = ThreatIntelligence('download_script.sh', '', 'feed_folder')
        with self.assertRaises(TypeError, msg="Expected TypeError for blank argument"):
            ti = ThreatIntelligence('download_script.sh', 'API_KEY', '')

if __name__ == '__main__':
    unittest.main()
