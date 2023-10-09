# Internet Festival 2023 - HighSchools CTF Workshop

## [crypto] Crittografia secondo i film (10 risoluzioni)

Il testo cifrato è ottenuto codificando la flag con base64 ed hex numerose volte. Per decodificare è sufficiente incollare il testo cifrato su CyberChef, che automaticamente riconoscerà la codifica e premendo la bacchetta magica accanto ad "Output" effetuerà la decodifica. L'ultimo step è semplicemente rot13, anche quest'ultimo facilmente decodificabile da CyberChef.

Al seguente link si possono vedere tutti gli step applicati per la decodifica: [https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Hex('None')From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Hex('None')ROT13(true,true,false,13)&input=TlRRMlpUY3dOR1UwWkRNd016azFOVFUzTm1RM09EUm1OalUyWXpRMU4yRTFOelUzTnpBMVlUUmtOVFV6TlRNMk5UTTFORFJsTldFMU5qUTNOR1V6TlRVME5tRTBZVFEyTkdRMll6Y3dOekUxT1RNek5tTTBaall4Tm1NMU5UYzROVGMyWkRjd05tRTBaRFExTXpVM01UVmhOMkUwWVRWaE5qVTJZelppTnprMU5EWmpOalExWVRSa016QXpNVGN4TlRjMU9EWTROR1kyTlRaaU5EVTNPVFUwTlRjM01EWmhOalUwTlRNMU16WTFOelUwTkdFMFpUVTJORGMwWkRjM05UUTJaRGN3TldFMFpEVTJOekEzTVRVM05tUTNPRFJtTmpFMll6VTFOMkUxTkRVM056QTFOell5TlRVek5UY3hOVEkxTkRSaE5HVTJNVFpqTm1JM1lUVTBObU0yTkRWaE5HUXpNRE14TnpFMU56VTROamcwWmpZMU5tSTBOVGM1TlRRMll6VXlOakUyTVRaaU16VTNNVFUwTlRRMFlUUm1OalUyWkRSa056azFORFprTnpBMFlUUmtObUl6TVRVMU5UYzFORFJoTkdZMFpEWmpORFV6T1E9PQ](<https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Hex('None')From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Hex('None')ROT13(true,true,false,13)&input=TlRRMlpUY3dOR1UwWkRNd016azFOVFUzTm1RM09EUm1OalUyWXpRMU4yRTFOelUzTnpBMVlUUmtOVFV6TlRNMk5UTTFORFJsTldFMU5qUTNOR1V6TlRVME5tRTBZVFEyTkdRMll6Y3dOekUxT1RNek5tTTBaall4Tm1NMU5UYzROVGMyWkRjd05tRTBaRFExTXpVM01UVmhOMkUwWVRWaE5qVTJZelppTnprMU5EWmpOalExWVRSa016QXpNVGN4TlRjMU9EWTROR1kyTlRaaU5EVTNPVFUwTlRjM01EWmhOalUwTlRNMU16WTFOelUwTkdFMFpUVTJORGMwWkRjM05UUTJaRGN3TldFMFpEVTJOekEzTVRVM05tUTNPRFJtTmpFMll6VTFOMkUxTkRVM056QTFOell5TlRVek5UY3hOVEkxTkRSaE5HVTJNVFpqTm1JM1lUVTBObU0yTkRWaE5HUXpNRE14TnpFMU56VTROamcwWmpZMU5tSTBOVGM1TlRRMll6VXlOakUyTVRaaU16VTNNVFUwTlRRMFlUUm1OalUyWkRSa056azFORFprTnpBMFlUUmtObUl6TVRVMU5UYzFORFJoTkdZMFpEWmpORFV6T1E9PQ>)